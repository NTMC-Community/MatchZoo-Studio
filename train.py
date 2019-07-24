import os
import sys
import json
from flask import request, Blueprint, jsonify
from matchzoo_api import (
    dssm_api, drmm_api, cdssm_api, arcii_api, matchpyramid_api,
    duet_api, mvlstm_api, arci_api, krnm_api, conv_knrm_api
)
from utils import json_read, json_write, IOpool, LogDir, format_stringio_to_json, convert_to_right_type


main = Blueprint('train', __name__)
ROOT_PATH = sys.path[0] + '/'


@main.route('/head/<string:model>', methods=['POST'])
def MODEL_HEAD(model):
    print('model is : ' + model)
    request_data = json.loads(request.data.decode('utf-8'))
    train_id = request_data['train_id']
    print(request_data)
    parameter = {}
    for kvs in request_data['parameter'].keys():
        parameter[kvs] = request_data['parameter'][kvs]
    file_name = ROOT_PATH + 'matchzoo_temp_files/data/' + train_id + '.json'
    dataset_path = ROOT_PATH + 'matchzoo_temp_files/files/' + train_id + '.train'
    init_dict = {
        'state': 'run',
        'data': {
            'loss': [[]],
            'accuracy': [[], [], []]
        }
    }
    model_name = ['dssm', 'drmm', 'cdssm', 'arcii', 'matchpyramid',
                  'duet', 'mvlstm', 'arci', 'krnm', 'conv_knrm']
    model_api = [dssm_api, drmm_api, cdssm_api, arcii_api, matchpyramid_api,
                 duet_api, mvlstm_api, arci_api, krnm_api, conv_knrm_api]
    if not os.path.exists(file_name):
        json_write(file_name, init_dict)
        with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + train_id + '.log', 'w') as f:
            f.write('')
        with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + train_id + '.preprocess_log', 'w') as f:
            f.write('')
        qpool = IOpool()
        logdir = LogDir()
        for idx in range(len(model_name)):
            if model_name[idx] == model:
                model_api[idx](qpool, logdir, dataset_path, train_id, parameter)
                break
    return jsonify({'status': 'ok'})


@main.route('/query/<string:model>', methods=['POST'])  # file_name是结果json文件的路径，dataset_path是训练集的路径
def MODEL_QEURY(model):
    request_data = json.loads(request.data.decode('utf-8'))
    train_id = request_data['train_id']
    epochs = request_data['epochs']
    file_name = ROOT_PATH + 'matchzoo_temp_files/data/' + train_id + '.json'
    format_stringio_to_json(train_id, file_name, epochs)  # 由logger得到目标的json文件
    try:
        ret_data = json_read(file_name)
        return jsonify(ret_data)
    except:
        ret_data = {}
        return jsonify(ret_data)
