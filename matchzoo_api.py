import numpy as np
import matchzoo as mz
import keras
import sys
from utils import load_train_data, load_test_data

ROOT_PATH = sys.path[0] + '/'


def dssm_api(qpool, logdir, dataset_path, train_id, parameter):
    keras.backend.clear_session()
    # load数据并创建preprocessor对象
    train_pack = load_train_data(train_id, parameter['existing_dataset'], parameter['task'])
    predict_pack = load_test_data(train_id, parameter['existing_dataset'], parameter['task'])
    preprocessor = mz.preprocessors.DSSMPreprocessor()
    # 重定向stderr到log文件
    logdir.set_preprocess_id(train_id)
    err_old = sys.stderr
    sys.stderr = logdir
    # preprocessor.fit的内容写出到log，写完后关闭重定向，保存preprocessor
    train_pack_processed = preprocessor.fit_transform(train_pack)
    sys.stderr = err_old
    preprocessor.save(ROOT_PATH + 'matchzoo_temp_files/preprocessors/' + train_id + '.dssm_preprocessor')
    predict_pack_processed = preprocessor.transform(predict_pack)
    with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + train_id + '.preprocess_log', 'a') as f:
        f.write('Preprocess finished!')
    ranking_task = mz.tasks.Ranking(loss=mz.losses.RankCrossEntropyLoss(num_neg=4))
    ranking_task.metrics = [
        mz.metrics.NormalizedDiscountedCumulativeGain(k=3),
        mz.metrics.NormalizedDiscountedCumulativeGain(k=5),
        mz.metrics.MeanAveragePrecision()
    ]
    model = mz.models.DSSM()
    model.params['input_shapes'] = preprocessor.context['input_shapes']
    model.params['task'] = ranking_task
    model.params['mlp_num_layers'] = parameter['mlp_num_layers']
    model.params['mlp_num_units'] = parameter['mlp_num_units']
    model.params['mlp_num_fan_out'] = parameter['mlp_num_fan_out']
    model.params['mlp_activation_func'] = parameter['mlp_activation_func']
    model.guess_and_fill_missing_params()
    model.build()
    model.compile()
    model.backend.summary()
    pred_x, pred_y = predict_pack_processed[:].unpack()
    evaluate = mz.callbacks.EvaluateAllMetrics(model, x=pred_x, y=pred_y, batch_size=len(pred_x))
    train_generator = mz.PairDataGenerator(train_pack_processed, num_dup=1, num_neg=4, batch_size=64, shuffle=True)
    # 重定向stdout到log当中
    qpool.set_trainid(train_id)
    old = sys.stdout
    sys.stdout = qpool
    model.fit_generator(train_generator, epochs=parameter['epochs'], callbacks=[evaluate], workers=5, use_multiprocessing=False)
    sys.stdout = old
    model.save(ROOT_PATH + 'matchzoo_temp_files/models/' + train_id + '.dssm_model')


def drmm_api(qpool, logdir, dataset_path, train_id, parameter):
    keras.backend.clear_session()
    # load数据并创建preprocessor对象
    train_pack = load_train_data(train_id, parameter['existing_dataset'], parameter['task'])
    predict_pack = load_test_data(train_id, parameter['existing_dataset'], parameter['task'])
    preprocessor = mz.preprocessors.BasicPreprocessor(fixed_length_left=10, fixed_length_right=100,
                                                      remove_stop_words=False)
    # 重定向stderr到log文件
    logdir.set_preprocess_id(train_id)
    err_old = sys.stderr
    sys.stderr = logdir
    # preprocessor.fit的内容写出到log，写完后关闭重定向，保存preprocessor
    train_pack_processed = preprocessor.fit_transform(train_pack)
    sys.stderr = err_old
    preprocessor.save(ROOT_PATH + 'matchzoo_temp_files/preprocessors/' + train_id + '.drmm_preprocessor')
    predict_pack_processed = preprocessor.transform(predict_pack)
    with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + train_id + '.preprocess_log', 'a') as f:
        f.write('Preprocess finished!')
    ranking_task = mz.tasks.Ranking(loss=mz.losses.RankHingeLoss())
    ranking_task.metrics = [
        mz.metrics.NormalizedDiscountedCumulativeGain(k=3),
        mz.metrics.NormalizedDiscountedCumulativeGain(k=5),
        mz.metrics.MeanAveragePrecision()
    ]
    model = mz.models.DRMMTKS()
    bin_size = 30
    #model.params['input_shapes'] = [[10, ], [10, bin_size, ]]
    model.params.update(preprocessor.context)
    model.params['task'] = ranking_task
    model.params['mask_value'] = parameter['mask_value']
    model.params['embedding_input_dim'] = preprocessor.context['vocab_size']
    model.params['embedding_output_dim'] = parameter['embedding_output_dim']
    model.params['mlp_num_layers'] = parameter['mlp_num_layers']
    model.params['mlp_num_units'] = parameter['mlp_num_units']
    model.params['mlp_num_fan_out'] = parameter['mlp_num_fan_out']
    model.params['top_k'] = parameter['top_k']
    model.params['mlp_activation_func'] = 'relu'
    model.params['optimizer'] = 'adadelta'
    model.guess_and_fill_missing_params()
    model.build()
    model.compile()
    model.backend.summary()
    glove_embedding = mz.datasets.embeddings.load_glove_embedding(dimension=300)
    embedding_matrix = glove_embedding.build_matrix(preprocessor.context['vocab_unit'].state['term_index'])
    l2_norm = np.sqrt((embedding_matrix * embedding_matrix).sum(axis=1))
    embedding_matrix = embedding_matrix / l2_norm[:, np.newaxis]
    model.load_embedding_matrix(embedding_matrix)
    '''
    pred_generator = mz.HistogramDataGenerator(data_pack=predict_pack_processed,
                                               embedding_matrix=embedding_matrix,
                                               bin_size=bin_size,
                                               hist_mode='LCH')
    pred_x, pred_y = pred_generator[:]
    '''
    pred_x, pred_y = predict_pack_processed.unpack()
    evaluate = mz.callbacks.EvaluateAllMetrics(model,
                                               x=pred_x,
                                               y=pred_y,
                                               once_every=1,
                                               batch_size=len(pred_y)
                                               )
    train_generator = mz.DataGenerator(train_pack_processed, mode='pair',
                                                    num_dup=2, num_neg=1, batch_size=20)
    # 重定向stdout到log当中
    qpool.set_trainid(train_id)
    old = sys.stdout
    sys.stdout = qpool
    model.fit_generator(train_generator, epochs=parameter['epochs'], callbacks=[evaluate], workers=5, use_multiprocessing=False)
    sys.stdout = old
    model.save(ROOT_PATH + 'matchzoo_temp_files/models/' + train_id + '.drmm_model')


def drmm_bak_api(qpool, logdir, dataset_path, train_id, parameter):
    keras.backend.clear_session()
    # load数据并创建preprocessor对象
    train_pack = load_train_data(train_id, parameter['existing_dataset'], parameter['task'])
    predict_pack = load_test_data(train_id, parameter['existing_dataset'], parameter['task'])
    preprocessor = mz.preprocessors.BasicPreprocessor(fixed_length_left=10, fixed_length_right=100,
                                                      remove_stop_words=False)
    # 重定向stderr到log文件
    logdir.set_preprocess_id(train_id)
    err_old = sys.stderr
    sys.stderr = logdir
    # preprocessor.fit的内容写出到log，写完后关闭重定向，保存preprocessor
    train_pack_processed = preprocessor.fit_transform(train_pack)
    sys.stderr = err_old
    preprocessor.save(ROOT_PATH + 'matchzoo_temp_files/preprocessors/' + train_id + '.drmm_preprocessor')
    predict_pack_processed = preprocessor.transform(predict_pack)
    with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + train_id + '.preprocess_log', 'a') as f:
        f.write('Preprocess finished!')
    ranking_task = mz.tasks.Ranking(loss=mz.losses.RankCrossEntropyLoss(num_neg=4))
    ranking_task.metrics = [
        mz.metrics.NormalizedDiscountedCumulativeGain(k=3),
        mz.metrics.NormalizedDiscountedCumulativeGain(k=5),
        mz.metrics.MeanAveragePrecision()
    ]
    model = mz.models.DRMM()
    bin_size = 30
    model.params['input_shapes'] = [[10, ], [10, bin_size, ]]
    model.params['task'] = ranking_task
    model.params['mask_value'] = parameter['mask_value']
    model.params['embedding_input_dim'] = preprocessor.context['vocab_size']
    model.params['embedding_output_dim'] = parameter['embedding_output_dim']
    model.params['mlp_num_layers'] = parameter['mlp_num_layers']
    model.params['mlp_num_units'] = parameter['mlp_num_units']
    model.params['mlp_num_fan_out'] = parameter['mlp_num_fan_out']
    model.params['top_k'] = parameter['top_k']
    model.params['mlp_activation_func'] = 'tanh'
    model.params['optimizer'] = 'adadelta'
    model.guess_and_fill_missing_params()
    model.build()
    model.compile()
    model.backend.summary()
    glove_embedding = mz.datasets.embeddings.load_glove_embedding(dimension=300)
    embedding_matrix = glove_embedding.build_matrix(preprocessor.context['vocab_unit'].state['term_index'])
    l2_norm = np.sqrt((embedding_matrix * embedding_matrix).sum(axis=1))
    embedding_matrix = embedding_matrix / l2_norm[:, np.newaxis]
    model.load_embedding_matrix(embedding_matrix)
    pred_generator = mz.HistogramDataGenerator(data_pack=predict_pack_processed,
                                               embedding_matrix=embedding_matrix,
                                               bin_size=bin_size,
                                               hist_mode='LCH')
    pred_x, pred_y = pred_generator[:]
    evaluate = mz.callbacks.EvaluateAllMetrics(model,
                                               x=pred_x,
                                               y=pred_y,
                                               once_every=1,
                                               batch_size=len(pred_y)
                                               )
    train_generator = mz.HistogramPairDataGenerator(train_pack_processed, embedding_matrix, bin_size, 'LCH',
                                                    num_dup=2, num_neg=4, batch_size=20)
    # 重定向stdout到log当中
    qpool.set_trainid(train_id)
    old = sys.stdout
    sys.stdout = qpool
    model.fit_generator(train_generator, epochs=parameter['epochs'], callbacks=[evaluate], workers=5, use_multiprocessing=False)
    sys.stdout = old
    model.save(ROOT_PATH + 'matchzoo_temp_files/models/' + train_id + '.drmm_model')


def cdssm_api(qpool, logdir, dataset_path, train_id, parameter):
    keras.backend.clear_session()
    # load数据并创建preprocessor对象
    train_pack = load_train_data(train_id, parameter['existing_dataset'], parameter['task'])
    predict_pack = load_test_data(train_id, parameter['existing_dataset'], parameter['task'])
    preprocessor = mz.preprocessors.CDSSMPreprocessor()
    # 重定向stderr到log文件
    logdir.set_preprocess_id(train_id)
    err_old = sys.stderr
    sys.stderr = logdir
    # preprocessor.fit的内容写出到log，写完后关闭重定向，保存preprocessor
    train_pack_processed = preprocessor.fit_transform(train_pack)
    sys.stderr = err_old
    preprocessor.save(ROOT_PATH + 'matchzoo_temp_files/preprocessors/' + train_id + '.cdssm_preprocessor')
    predict_pack_processed = preprocessor.transform(predict_pack)
    with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + train_id + '.preprocess_log', 'a') as f:
        f.write('Preprocess finished!')
    ranking_task = mz.tasks.Ranking(loss=mz.losses.RankCrossEntropyLoss(num_neg=4))
    ranking_task.metrics = [
        mz.metrics.NormalizedDiscountedCumulativeGain(k=3),
        mz.metrics.NormalizedDiscountedCumulativeGain(k=5),
        mz.metrics.MeanAveragePrecision()
    ]
    model = mz.models.CDSSM()
    model.params['input_shapes'] = preprocessor.context['input_shapes']
    model.params['task'] = ranking_task
    model.params['filters'] = parameter['filters']
    model.params['kernel_size'] = parameter['kernel_size']
    model.params['strides'] = parameter['strides']
    model.params['padding'] = parameter['padding']
    model.params['conv_activation_func'] = parameter['conv_activation_func']
    model.params['w_initializer'] = parameter['w_initializer']
    model.params['b_initializer'] = parameter['b_initializer']
    model.params['mlp_num_layers'] = parameter['mlp_num_layers']
    model.params['mlp_num_units'] = parameter['mlp_num_units']
    model.params['mlp_num_fan_out'] = parameter['mlp_num_fan_out']
    model.params['mlp_activation_func'] = parameter['mlp_activation_func']
    model.params['dropout_rate'] = 0.8
    model.params['optimizer'] = 'adadelta'
    model.guess_and_fill_missing_params()
    model.guess_and_fill_missing_params()
    model.build()
    model.compile()
    model.backend.summary()
    pred_x, pred_y = predict_pack_processed[:].unpack()
    evaluate = mz.callbacks.EvaluateAllMetrics(model, x=pred_x, y=pred_y, batch_size=len(pred_x))
    train_generator = mz.PairDataGenerator(train_pack_processed, num_dup=1, num_neg=4, batch_size=64, shuffle=True)
    # 重定向stdout到log当中
    qpool.set_trainid(train_id)
    old = sys.stdout
    sys.stdout = qpool
    model.fit_generator(train_generator, epochs=parameter['epochs'], callbacks=[evaluate], workers=5, use_multiprocessing=False)
    sys.stdout = old
    model.save(ROOT_PATH + 'matchzoo_temp_files/models/' + train_id + '.cdssm_model')


def arcii_api(qpool, logdir, dataset_path, train_id, parameter):
    keras.backend.clear_session()
    # load数据并创建preprocessor对象
    train_pack = load_train_data(train_id, parameter['existing_dataset'], parameter['task'])
    predict_pack = load_test_data(train_id, parameter['existing_dataset'], parameter['task'])
    preprocessor = mz.preprocessors.BasicPreprocessor(fixed_length_left=10, fixed_length_right=100,
                                                      remove_stop_words=False)
    # 重定向stderr到log文件
    logdir.set_preprocess_id(train_id)
    err_old = sys.stderr
    sys.stderr = logdir
    # preprocessor.fit的内容写出到log，写完后关闭重定向，保存preprocessor
    train_pack_processed = preprocessor.fit_transform(train_pack)
    sys.stderr = err_old
    preprocessor.save(ROOT_PATH + 'matchzoo_temp_files/preprocessors/' + train_id + '.arcii_preprocessor')
    predict_pack_processed = preprocessor.transform(predict_pack)
    with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + train_id + '.preprocess_log', 'a') as f:
        f.write('Preprocess finished!')
    ranking_task = mz.tasks.Ranking(loss=mz.losses.RankHingeLoss())
    ranking_task.metrics = [
        mz.metrics.NormalizedDiscountedCumulativeGain(k=3),
        mz.metrics.NormalizedDiscountedCumulativeGain(k=5),
        mz.metrics.MeanAveragePrecision()
    ]
    model = mz.models.ArcII()
    model.params['input_shapes'] = preprocessor.context['input_shapes']
    model.params['task'] = ranking_task
    model.params['embedding_input_dim'] = preprocessor.context['vocab_size']
    model.params['embedding_output_dim'] = parameter['embedding_output_dim']
    model.params['embedding_trainable'] = True
    model.params['num_blocks'] = parameter['num_blocks']
    model.params['kernel_1d_count'] = parameter['kernel_1d_count']
    model.params['kernel_1d_size'] = parameter['kernel_1d_size']
    model.params['kernel_2d_count'] = [64, 64]
    model.params['kernel_2d_size'] = [3, 3]
    model.params['pool_2d_size'] = [[3, 3], [3, 3]]
    model.params['optimizer'] = 'adam'
    model.guess_and_fill_missing_params()
    model.build()
    model.compile()
    model.backend.summary()
    glove_embedding = mz.datasets.embeddings.load_glove_embedding(dimension=300)
    embedding_matrix = glove_embedding.build_matrix(preprocessor.context['vocab_unit'].state['term_index'])
    model.load_embedding_matrix(embedding_matrix)
    pred_x, pred_y = predict_pack_processed[:].unpack()
    evaluate = mz.callbacks.EvaluateAllMetrics(model, x=pred_x, y=pred_y, batch_size=len(pred_y))
    train_generator = mz.PairDataGenerator(train_pack_processed, num_dup=2, num_neg=1, batch_size=20)
    # 重定向stdout到log当中
    qpool.set_trainid(train_id)
    old = sys.stdout
    sys.stdout = qpool
    model.fit_generator(train_generator, epochs=parameter['epochs'], callbacks=[evaluate], workers=5, use_multiprocessing=False)
    sys.stdout = old
    model.save(ROOT_PATH + 'matchzoo_temp_files/models/' + train_id + '.arcii_model')


def matchpyramid_api(qpool, logdir, dataset_path, train_id, parameter):
    keras.backend.clear_session()
    # load数据并创建preprocessor对象
    train_pack = load_train_data(train_id, parameter['existing_dataset'], parameter['task'])
    predict_pack = load_test_data(train_id, parameter['existing_dataset'], parameter['task'])
    preprocessor = mz.preprocessors.BasicPreprocessor(fixed_length_left=10, fixed_length_right=40,
                                                      remove_stop_words=True)
    # 重定向stderr到log文件
    logdir.set_preprocess_id(train_id)
    err_old = sys.stderr
    sys.stderr = logdir
    # preprocessor.fit的内容写出到log，写完后关闭重定向，保存preprocessor
    train_pack_processed = preprocessor.fit_transform(train_pack)
    sys.stderr = err_old
    preprocessor.save(ROOT_PATH + 'matchzoo_temp_files/preprocessors/' + train_id + '.matchpyramid_preprocessor')
    predict_pack_processed = preprocessor.transform(predict_pack)
    with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + train_id + '.preprocess_log', 'a') as f:
        f.write('Preprocess finished!')
    ranking_task = mz.tasks.Ranking(loss=mz.losses.RankHingeLoss())
    ranking_task.metrics = [
        mz.metrics.NormalizedDiscountedCumulativeGain(k=3),
        mz.metrics.NormalizedDiscountedCumulativeGain(k=5),
        mz.metrics.MeanAveragePrecision()
    ]
    model = mz.models.MatchPyramid()
    model.params['input_shapes'] = preprocessor.context['input_shapes']
    model.params['task'] = ranking_task
    model.params['embedding_input_dim'] = preprocessor.context['vocab_size']
    model.params['embedding_output_dim'] = parameter['embedding_output_dim']
    model.params['embedding_trainable'] = True
    model.params['num_blocks'] = parameter['num_blocks']
    model.params['kernel_count'] = [16, 32]
    model.params['kernel_size'] = [[3, 3], [3, 3]]
    model.params['dpool_size'] = [3, 10]
    model.params['optimizer'] = 'adam'
    model.params['dropout_rate'] = 0.1
    model.guess_and_fill_missing_params()
    model.build()
    model.compile()
    model.backend.summary()
    glove_embedding = mz.datasets.embeddings.load_glove_embedding(dimension=300)
    embedding_matrix = glove_embedding.build_matrix(preprocessor.context['vocab_unit'].state['term_index'])
    model.load_embedding_matrix(embedding_matrix)

    train_generator = mz.DPoolPairDataGenerator(train_pack_processed,
                                                fixed_length_left=10,
                                                fixed_length_right=40,
                                                num_dup=2,
                                                num_neg=1,
                                                batch_size=20)
    predict_generator = mz.DPoolDataGenerator(predict_pack_processed,
                                              fixed_length_left=10,
                                              fixed_length_right=40,
                                              batch_size=20)
    pred_x, pred_y = predict_generator[:]
    evaluate = mz.callbacks.EvaluateAllMetrics(model, x=pred_x, y=pred_y, batch_size=len(pred_y))
    # 重定向stdout到log当中
    qpool.set_trainid(train_id)
    old = sys.stdout
    sys.stdout = qpool
    model.fit_generator(train_generator, epochs=parameter['epochs'], callbacks=[evaluate], workers=5, use_multiprocessing=False)
    sys.stdout = old
    model.save(ROOT_PATH + 'matchzoo_temp_files/models/' + train_id + '.matchpyramid_model')


def duet_api(qpool, logdir, dataset_path, train_id, parameter):
    keras.backend.clear_session()
    # load数据并创建preprocessor对象
    train_pack = load_train_data(train_id, parameter['existing_dataset'], parameter['task'])
    predict_pack = load_test_data(train_id, parameter['existing_dataset'], parameter['task'])

    preprocessor = mz.preprocessors.BasicPreprocessor(fixed_length_left=10, fixed_length_right=40,
                                                      remove_stop_words=False)
    # 重定向stderr到log文件
    logdir.set_preprocess_id(train_id)
    err_old = sys.stderr
    sys.stderr = logdir
    # preprocessor.fit的内容写出到log，写完后关闭重定向，保存preprocessor
    train_pack_processed = preprocessor.fit_transform(train_pack)
    sys.stderr = err_old
    preprocessor.save(ROOT_PATH + 'matchzoo_temp_files/preprocessors/' + train_id + '.duet_preprocessor')
    predict_pack_processed = preprocessor.transform(predict_pack)
    with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + train_id + '.preprocess_log', 'a') as f:
        f.write('Preprocess finished!')
    ranking_task = mz.tasks.Ranking(loss=mz.losses.RankHingeLoss())
    ranking_task.metrics = [
        mz.metrics.NormalizedDiscountedCumulativeGain(k=3),
        mz.metrics.NormalizedDiscountedCumulativeGain(k=5),
        mz.metrics.MeanAveragePrecision()
    ]
    model = mz.models.DUET()
    model.params['input_shapes'] = preprocessor.context['input_shapes']
    model.params['task'] = ranking_task
    model.params['embedding_input_dim'] = preprocessor.context['vocab_size']
    model.params['embedding_output_dim'] = parameter['embedding_output_dim']
    model.params['lm_filters'] = parameter['lm_filters']
    model.params['lm_hidden_sizes'] = [parameter['lm_hidden_sizes']]
    model.params['dm_filters'] = parameter['dm_filters']
    model.params['dm_kernel_size'] = parameter['dm_kernel_size']
    model.params['dm_d_mpool'] = parameter['dm_d_mpool']
    model.params['dm_hidden_sizes'] = [parameter['dm_hidden_sizes']]
    model.params['dropout_rate'] = 0.5
    model.params['optimizer'] = 'adagrad'
    model.guess_and_fill_missing_params()
    model.build()
    model.compile()
    model.backend.summary()
    glove_embedding = mz.datasets.embeddings.load_glove_embedding(dimension=300)
    embedding_matrix = glove_embedding.build_matrix(preprocessor.context['vocab_unit'].state['term_index'])
    model.load_embedding_matrix(embedding_matrix)
    pred_x, pred_y = predict_pack_processed[:].unpack()
    evaluate = mz.callbacks.EvaluateAllMetrics(model, x=pred_x, y=pred_y, batch_size=len(pred_y))
    train_generator = mz.PairDataGenerator(train_pack_processed, num_dup=2, num_neg=1, batch_size=20)
    # 重定向stdout到log当中
    qpool.set_trainid(train_id)
    old = sys.stdout
    sys.stdout = qpool
    model.fit_generator(train_generator, epochs=parameter['epochs'], callbacks=[evaluate], workers=5, use_multiprocessing=False)
    sys.stdout = old
    model.save(ROOT_PATH + 'matchzoo_temp_files/models/' + train_id + '.duet_model')


def mvlstm_api(qpool, logdir, dataset_path, train_id, parameter):
    keras.backend.clear_session()
    # load数据并创建preprocessor对象
    train_pack = load_train_data(train_id, parameter['existing_dataset'], parameter['task'])
    predict_pack = load_test_data(train_id, parameter['existing_dataset'], parameter['task'])

    preprocessor = mz.preprocessors.BasicPreprocessor(fixed_length_left=10, fixed_length_right=40,
                                                      remove_stop_words=False)
    # 重定向stderr到log文件
    logdir.set_preprocess_id(train_id)
    err_old = sys.stderr
    sys.stderr = logdir
    # preprocessor.fit的内容写出到log，写完后关闭重定向，保存preprocessor
    train_pack_processed = preprocessor.fit_transform(train_pack)
    sys.stderr = err_old
    preprocessor.save(ROOT_PATH + 'matchzoo_temp_files/preprocessors/' + train_id + '.mvlstm_preprocessor')
    predict_pack_processed = preprocessor.transform(predict_pack)
    with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + train_id + '.preprocess_log', 'a') as f:
        f.write('Preprocess finished!')
    ranking_task = mz.tasks.Ranking(loss=mz.losses.RankHingeLoss())
    ranking_task.metrics = [
        mz.metrics.NormalizedDiscountedCumulativeGain(k=3),
        mz.metrics.NormalizedDiscountedCumulativeGain(k=5),
        mz.metrics.MeanAveragePrecision()
    ]
    model = mz.models.MVLSTM()
    model.params['input_shapes'] = preprocessor.context['input_shapes']
    model.params['task'] = ranking_task
    model.params['embedding_input_dim'] = preprocessor.context['vocab_size']
    model.params['embedding_output_dim'] = parameter['embedding_output_dim']
    model.params['lstm_units'] = parameter['lstm_units']
    model.params['top_k'] = parameter['top_k']
    model.params['mlp_num_layers'] = parameter['mlp_num_layers']
    model.params['mlp_num_units'] = parameter['mlp_num_units']
    model.params['mlp_num_fan_out'] = parameter['mlp_num_fan_out']
    model.params['mlp_activation_func'] = 'relu'
    model.params['dropout_rate'] = 0.5
    model.params['optimizer'] = 'adadelta'
    model.guess_and_fill_missing_params()
    model.build()
    model.compile()
    model.backend.summary()
    glove_embedding = mz.datasets.embeddings.load_glove_embedding(dimension=100)
    embedding_matrix = glove_embedding.build_matrix(preprocessor.context['vocab_unit'].state['term_index'])
    model.load_embedding_matrix(embedding_matrix)
    pred_x, pred_y = predict_pack_processed[:].unpack()
    evaluate = mz.callbacks.EvaluateAllMetrics(model, x=pred_x, y=pred_y, batch_size=len(pred_y))
    train_generator = mz.PairDataGenerator(train_pack_processed, num_dup=2, num_neg=1, batch_size=20)
    # 重定向stdout到log当中
    qpool.set_trainid(train_id)
    old = sys.stdout
    sys.stdout = qpool
    model.fit_generator(train_generator, epochs=parameter['epochs'], callbacks=[evaluate], workers=5, use_multiprocessing=False)
    sys.stdout = old
    model.save(ROOT_PATH + 'matchzoo_temp_files/models/' + train_id + '.mvlstm_model')


def arci_api(qpool, logdir, dataset_path, train_id, parameter):
    keras.backend.clear_session()
    # load数据并创建preprocessor对象
    train_pack = load_train_data(train_id, parameter['existing_dataset'], parameter['task'])
    predict_pack = load_test_data(train_id, parameter['existing_dataset'], parameter['task'])
    preprocessor = mz.preprocessors.BasicPreprocessor(fixed_length_left=10, fixed_length_right=100,
                                                      remove_stop_words=False)
    # 重定向stderr到log文件
    logdir.set_preprocess_id(train_id)
    err_old = sys.stderr
    sys.stderr = logdir
    # preprocessor.fit的内容写出到log，写完后关闭重定向，保存preprocessor
    train_pack_processed = preprocessor.fit_transform(train_pack)
    sys.stderr = err_old
    preprocessor.save(ROOT_PATH + 'matchzoo_temp_files/preprocessors/' + train_id + '.arci_preprocessor')
    predict_pack_processed = preprocessor.transform(predict_pack)
    with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + train_id + '.preprocess_log', 'a') as f:
        f.write('Preprocess finished!')
    ranking_task = mz.tasks.Ranking(loss=mz.losses.RankHingeLoss())
    ranking_task.metrics = [
        mz.metrics.NormalizedDiscountedCumulativeGain(k=3),
        mz.metrics.NormalizedDiscountedCumulativeGain(k=5),
        mz.metrics.MeanAveragePrecision()
    ]
    model = mz.models.ArcI()
    model.params['input_shapes'] = preprocessor.context['input_shapes']
    model.params['task'] = ranking_task
    model.params['embedding_input_dim'] = preprocessor.context['vocab_size']
    model.params['embedding_output_dim'] = parameter['embedding_output_dim']
    model.params['num_blocks'] = parameter['num_blocks']
    model.params['left_filters'] = [parameter['left_filters']]
    model.params['left_kernel_sizes'] = [parameter['left_kernel_sizes']]
    model.params['left_pool_sizes'] = [parameter['left_pool_sizes']]
    model.params['right_filters'] = [parameter['right_filters']]
    model.params['right_kernel_sizes'] = [parameter['right_kernel_sizes']]
    model.params['right_pool_sizes'] = [parameter['right_pool_sizes']]
    model.params['conv_activation_func'] = 'relu'
    model.params['mlp_num_layers'] = parameter['mlp_num_layers']
    model.params['mlp_num_units'] = parameter['mlp_num_units']
    model.params['mlp_num_fan_out'] = parameter['mlp_num_fan_out']
    model.params['mlp_activation_func'] = 'relu'
    model.params['dropout_rate'] = 0.9
    model.params['optimizer'] = 'adadelta'
    model.guess_and_fill_missing_params()
    model.build()
    model.compile()
    model.backend.summary()
    glove_embedding = mz.datasets.embeddings.load_glove_embedding(dimension=300)
    embedding_matrix = glove_embedding.build_matrix(preprocessor.context['vocab_unit'].state['term_index'])
    model.load_embedding_matrix(embedding_matrix)
    pred_x, pred_y = predict_pack_processed[:].unpack()
    evaluate = mz.callbacks.EvaluateAllMetrics(model, x=pred_x, y=pred_y, batch_size=len(pred_y))
    train_generator = mz.PairDataGenerator(train_pack_processed, num_dup=2, num_neg=1, batch_size=20)
    # 重定向stdout到log当中
    qpool.set_trainid(train_id)
    old = sys.stdout
    sys.stdout = qpool
    model.fit_generator(train_generator, epochs=parameter['epochs'], callbacks=[evaluate], workers=5, use_multiprocessing=False)
    sys.stdout = old
    model.save(ROOT_PATH + 'matchzoo_temp_files/models/' + train_id + '.arci_model')


def krnm_api(qpool, logdir, dataset_path, train_id, parameter):
    keras.backend.clear_session()
    # load数据并创建preprocessor对象
    train_pack = load_train_data(train_id, parameter['existing_dataset'], parameter['task'])
    predict_pack = load_test_data(train_id, parameter['existing_dataset'], parameter['task'])
    preprocessor = mz.preprocessors.BasicPreprocessor(fixed_length_left=10, fixed_length_right=100,
                                                      remove_stop_words=False)
    # 重定向stderr到log文件
    logdir.set_preprocess_id(train_id)
    err_old = sys.stderr
    sys.stderr = logdir
    # preprocessor.fit的内容写出到log，写完后关闭重定向，保存preprocessor
    train_pack_processed = preprocessor.fit_transform(train_pack)
    sys.stderr = err_old
    preprocessor.save(ROOT_PATH + 'matchzoo_temp_files/preprocessors/' + train_id + '.krnm_preprocessor')
    predict_pack_processed = preprocessor.transform(predict_pack)
    with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + train_id + '.preprocess_log', 'a') as f:
        f.write('Preprocess finished!')
    ranking_task = mz.tasks.Ranking(loss=mz.losses.RankHingeLoss())
    ranking_task.metrics = [
        mz.metrics.NormalizedDiscountedCumulativeGain(k=3),
        mz.metrics.NormalizedDiscountedCumulativeGain(k=5),
        mz.metrics.MeanAveragePrecision()
    ]

    model = mz.models.KNRM()
    model.params['input_shapes'] = preprocessor.context['input_shapes']
    model.params['task'] = ranking_task
    model.params['embedding_input_dim'] = preprocessor.context['vocab_size']
    model.params['embedding_output_dim'] = parameter['embedding_output_dim']
    model.params['embedding_trainable'] = True
    model.params['kernel_num'] = parameter['kernel_num']
    model.params['sigma'] = 0.1
    model.params['exact_sigma'] = 0.001
    model.params['optimizer'] = 'adadelta'
    model.guess_and_fill_missing_params()
    model.build()
    model.compile()
    model.backend.summary()
    glove_embedding = mz.datasets.embeddings.load_glove_embedding(dimension=300)
    embedding_matrix = glove_embedding.build_matrix(preprocessor.context['vocab_unit'].state['term_index'])
    model.load_embedding_matrix(embedding_matrix)
    pred_x, pred_y = predict_pack_processed[:].unpack()
    evaluate = mz.callbacks.EvaluateAllMetrics(model, x=pred_x, y=pred_y, batch_size=len(pred_y))
    train_generator = mz.PairDataGenerator(train_pack_processed, num_dup=2, num_neg=1, batch_size=20)
    # 重定向stdout到log当中
    qpool.set_trainid(train_id)
    old = sys.stdout
    sys.stdout = qpool
    model.fit_generator(train_generator, epochs=parameter['epochs'], callbacks=[evaluate], workers=5, use_multiprocessing=False)
    sys.stdout = old
    model.save(ROOT_PATH + 'matchzoo_temp_files/models/' + train_id + '.krnm_model')


def conv_knrm_api(qpool, logdir, dataset_path, train_id, parameter):
    keras.backend.clear_session()
    # load数据并创建preprocessor对象
    train_pack = load_train_data(train_id, parameter['existing_dataset'], parameter['task'])
    predict_pack = load_test_data(train_id, parameter['existing_dataset'], parameter['task'])
    preprocessor = mz.preprocessors.BasicPreprocessor(fixed_length_left=10, fixed_length_right=100,
                                                      remove_stop_words=False)
    # 重定向stderr到log文件
    logdir.set_preprocess_id(train_id)
    err_old = sys.stderr
    sys.stderr = logdir
    # preprocessor.fit的内容写出到log，写完后关闭重定向，保存preprocessor
    train_pack_processed = preprocessor.fit_transform(train_pack)
    sys.stderr = err_old
    preprocessor.save(ROOT_PATH + 'matchzoo_temp_files/preprocessors/' + train_id + '.conv_knrm_preprocessor')
    predict_pack_processed = preprocessor.transform(predict_pack)
    with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + train_id + '.preprocess_log', 'a') as f:
        f.write('Preprocess finished!')
    ranking_task = mz.tasks.Ranking(loss=mz.losses.RankHingeLoss())
    ranking_task.metrics = [
        mz.metrics.NormalizedDiscountedCumulativeGain(k=3),
        mz.metrics.NormalizedDiscountedCumulativeGain(k=5),
        mz.metrics.MeanAveragePrecision()
    ]

    model = mz.models.ConvKNRM()
    model.params['input_shapes'] = preprocessor.context['input_shapes']
    model.params['task'] = ranking_task
    model.params['embedding_input_dim'] = preprocessor.context['vocab_size']
    model.params['embedding_output_dim'] = 100 #parameter['embedding_output_dim']
    model.params['embedding_trainable'] = True
    model.params['filters'] = parameter['filters']
    model.params['conv_activation_func'] = 'tanh'
    model.params['max_ngram'] = parameter['max_ngram']
    model.params['use_crossmatch'] = True
    model.params['kernel_num'] = parameter['kernel_num']
    model.params['sigma'] = 0.1
    model.params['exact_sigma'] = 0.001
    model.params['optimizer'] = 'adadelta'
    model.guess_and_fill_missing_params()
    model.build()
    model.compile()
    model.backend.summary()
    glove_embedding = mz.datasets.embeddings.load_glove_embedding(dimension=100)
    embedding_matrix = glove_embedding.build_matrix(preprocessor.context['vocab_unit'].state['term_index'])
    model.load_embedding_matrix(embedding_matrix)
    pred_x, pred_y = predict_pack_processed[:].unpack()
    evaluate = mz.callbacks.EvaluateAllMetrics(model, x=pred_x, y=pred_y, batch_size=len(pred_y))
    train_generator = mz.PairDataGenerator(train_pack_processed, num_dup=2, num_neg=1, batch_size=20)
    # 重定向stdout到log当中
    qpool.set_trainid(train_id)
    old = sys.stdout
    sys.stdout = qpool
    model.fit_generator(train_generator, epochs=parameter['epochs'], callbacks=[evaluate], workers=5, use_multiprocessing=False)
    sys.stdout = old
    model.save(ROOT_PATH + 'matchzoo_temp_files/models/' + train_id + '.conv_knrm_model')
