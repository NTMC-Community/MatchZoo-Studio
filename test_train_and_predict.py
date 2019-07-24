import pandas as pd
import matchzoo as mz

ROOT_PATH = '/data/users/matchzoo/matchzoo-backend-ultimate/'


def train(train_id='test_file'):
    train_pack = mz.datasets.wiki_qa.load_data(stage='train')[:1000]
    dev_pack = mz.datasets.wiki_qa.load_data(stage='dev')[:1000]
    predict_pack = mz.datasets.wiki_qa.load_data(stage='test').drop_label()[:1000]

    preprocessor = mz.preprocessors.DSSMPreprocessor()
    preprocessor.fit(train_pack)
    preprocessor.save(ROOT_PATH + 'matchzoo_temp_files/preprocessors/' + train_id + '.dssm_preprocessor')

    train_pack_processed = preprocessor.transform(train_pack)
    dev_pack_processed = preprocessor.transform(dev_pack)

    train_generator = mz.PairDataGenerator(train_pack_processed, num_dup=5, num_neg=1, batch_size=32)

    ranking_task = mz.tasks.Ranking(loss=mz.losses.RankHingeLoss(num_neg=1, margin=1.0))
    ranking_task.metrics = [
        'mae', 'map', 'precision',
        mz.metrics.Precision(k=3),
        mz.metrics.DiscountedCumulativeGain(k=1),
        mz.metrics.DiscountedCumulativeGain(k=3),
        mz.metrics.DiscountedCumulativeGain(k=5),
        mz.metrics.NormalizedDiscountedCumulativeGain(k=1),
        mz.metrics.NormalizedDiscountedCumulativeGain(k=3),
        mz.metrics.NormalizedDiscountedCumulativeGain(k=5)
    ]

    model = mz.models.DSSMModel()
    model.params['task'] = ranking_task
    model.params['input_shapes'] = preprocessor.context['input_shapes']
    model.guess_and_fill_missing_params()
    model.build()
    model.compile()

    dev_x, dev_y = dev_pack_processed.unpack()
    evaluate = model.EvaluateOnCall(model, x=dev_x, y=dev_y, valid_steps=2, batch_size=32)
    model.fit(
        *train_pack_processed.unpack(),
        epochs=10,
        batch_size=32,
        callbacks=[evaluate]
    )

    model.save(ROOT_PATH + 'matchzoo_temp_files/models/' + train_id + '.dssm_model')

    model.fit_generator(
        train_generator,
        epochs=5,
        callbacks=[evaluate],
        workers=4,
        use_multiprocessing=True
    )


def predict(train_id='test_file'):
    q = 'how did apollo creed die'
    d = "Urban legend states that Apollo Creed's name is a wordplay on the Apostles' Creed , a statement of belief used in Christian churches."
    df = pd.DataFrame(data={'text_left': [q],
                            'text_right': [d],
                            'label': [0]})
    preprocessor = mz.load_preprocessor(ROOT_PATH + 'matchzoo_temp_files/preprocessors/' + train_id + '.dssm_preprocessor')
    predict_pack = mz.pack(df)
    predict_pack_processed = preprocessor.transform(predict_pack)
    model = mz.load_model(ROOT_PATH + 'matchzoo_temp_files/models/' + train_id + '.dssm_model')
    predict_score = float(model.predict(predict_pack_processed[:10].unpack()[0])[0][0])
    ret_dict = {
        'score': predict_score
    }
    print(ret_dict)


if __name__ == '__main__':
    id = 2
    if id == 1:
        train()
    elif id == 2:
        predict()
