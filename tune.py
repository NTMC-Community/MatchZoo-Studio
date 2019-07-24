import os
import sys
import json
import keras
import matchzoo as mz
from flask import request, Blueprint, jsonify
from utils import json_write, IOpool, LogDir


ROOT_PATH = sys.path[0] + '/'
main = Blueprint('tune', __name__)


def test():
    train_raw = mz.datasets.toy.load_data('train')
    dev_raw = mz.datasets.toy.load_data('dev')

    preprocessor = mz.preprocessors.BasicPreprocessor(fixed_length_left=10,
                                                      fixed_length_right=40,
                                                      remove_stop_words=True)
    train = preprocessor.fit_transform(train_raw, verbose=0)
    dev = preprocessor.transform(dev_raw, verbose=0)
    model = mz.models.MatchPyramid()

    model.params['input_shapes'] = preprocessor.context['input_shapes']
    model.params['task'] = mz.tasks.Ranking()
    model.guess_and_fill_missing_params()
    tuner = mz.auto.Tuner(
        params=model.params,
        train_data=train,
        test_data=dev,
        num_runs=5
    )
    results = tuner.tune()


def tune_api(qpool, logdir, dataset_path, train_id, parameter, epochs):
    keras.backend.clear_session()
    # 重定向输出
    logdir.set_preprocess_id(train_id)
    old = sys.stdout
    sys.stdout = logdir
    # 处理逻辑
    train_raw = mz.datasets.toy.load_data('train')
    dev_raw = mz.datasets.toy.load_data('dev')
    preprocessor = mz.models.DenseBaseline.get_default_preprocessor()
    train = preprocessor.fit_transform(train_raw, verbose=0)
    dev = preprocessor.transform(dev_raw, verbose=0)
    model_mapping = {
        'ARCI': mz.models.ArcI,
        'ARCII': mz.models.ArcII,
        'DSSM': mz.models.DSSM,
        'DRMM': mz.models.DRMMTKS,
        'CDSSM': mz.models.CDSSM,
        'MVLSTM': mz.models.MVLSTM,
        'DUET': mz.models.DUET,
        'KNRM': mz.models.KNRM,
        'CONVKNRM': mz.models.ConvKNRM
    }
    for ks in parameter:
        if parameter[ks]['chosen'] is True:
            print('======' + ks + '======')
            model = model_mapping[ks]()
            model.params['input_shapes'] = preprocessor.context['input_shapes']
            model.params['task'] = mz.tasks.Ranking()
            model.guess_and_fill_missing_params()

            param = parameter[ks]
            print(param)
            settings = {}
            for ks, vs in param.items():
                if ks == 'chosen':
                    continue
                elif ks == 'optimizer':
                    print(vs)
                    model.params.get('optimizer').hyper_space = mz.hyper_spaces.choice(vs)
                    continue
                lpos = ks.find('_low')
                hpos = ks.find('_high')
                if lpos != -1:
                    param_name = ks[:lpos]
                    if settings.get(param_name) is None:
                        settings[param_name] = [vs]
                    else:
                        settings[param_name].append(vs)
                else:
                    param_name = ks[:hpos]
                    if settings.get(param_name) is None:
                        settings[param_name] = [vs]
                    else:
                        settings[param_name].append(vs)
            for ks, vs in settings.items():
                vs.sort()
                # print(vs)
                if ks == 'dropout_rate':
                    step = 0.1
                elif ks == 'sigma':
                    step = 0.01
                else:
                    step = 1
                model.params.get(ks).hyper_space = mz.hyper_spaces.quniform(low=vs[0], high=vs[1], q=step)
            tuner = mz.auto.Tuner(
                params=model.params,
                train_data=train,
                test_data=dev,
                num_runs=epochs
            )
            results = tuner.tune()
    print('$$$finished$$$')
    # 还原输出
    sys.stderr = old


@main.route('/query', methods=['POST'])
def tune_query():
    request_data = json.loads(request.data.decode('utf-8'))
    train_id = request_data['tune_id']
    logger_name = os.path.join(ROOT_PATH, 'matchzoo_temp_files/logger/', train_id + '.preprocess_log')
    response = {
        'score': 0,
        'chart': [],
        'info': {},
        'state': 'run',
        'update': False
    }
    cur_model = ''
    epoch = -1
    best_score = request_data['best_score']
    keep_record = False
    with open(logger_name) as f:
        for line in f:
            if len(line) <= 1:
                continue
            if line[0:6] == '======':
                keep_record = False
                cur_model = line.split('======')[1]
                response['chart'].append([])
            elif line[0:5] == 'Run #':
                keep_record = False
                epoch = int(line.split('Run #')[1])
            elif line[0:7] == 'Score: ':
                score = float(line.split('Score: ')[1])
                if score > best_score:
                    best_score = score
                    keep_record = True
                    response['update'] = True
                response['chart'][-1].append({'x': epoch, 'y': score, 'm': cur_model})
            elif line == '$$$finished$$$\n':
                keep_record = False
                response['state'] = 'end'
            if keep_record is True:
                ssline = line.split()
                if len(ssline) == 2:
                    ks, vs = ssline[0], ssline[1]
                else:
                    ks = ssline[0]
                    vs = ' '.join(ssline[1:])
                response['info'][ks] = vs
    return jsonify(response)


@main.route('/head', methods=['POST'])
def tune():
    request_data = json.loads(request.data.decode('utf-8'))
    train_id = request_data['train_id']
    parameter = request_data['parameter']
    epochs = request_data['epochs']
    file_name = ROOT_PATH + 'matchzoo_temp_files/data/' + train_id + '.json'
    dataset_path = ROOT_PATH + 'matchzoo_temp_files/files/' + train_id + '.train'
    init_dict = {
        'state': 'run',
        'data': {
            'loss': [[]],
            'accuracy': [[], [], []]
        }
    }
    if not os.path.exists(file_name):
        json_write(file_name, init_dict)
        with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + train_id + '.preprocess_log', 'w') as f:
            f.write('')
        qpool = IOpool()
        logdir = LogDir()
        tune_api(qpool, logdir, dataset_path, train_id, parameter, epochs)
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    test()
