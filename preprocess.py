from flask import Blueprint, request, jsonify
import sys
import os
import json


main = Blueprint('preprocess', __name__)
ROOT_PATH = sys.path[0] + '/'


@main.route('/<string:model>', methods=['POST'])
def model_preprocess(model):
    request_data = json.loads(request.data.decode('utf-8'))
    preprocess_id = request_data['preprocess_id']
    ret_dict = {}
    with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + preprocess_id + '.preprocess_log') as f:
        content = f.readlines()
        ret_dict['console_list'] = content
    return jsonify(ret_dict)
