import keras
import matchzoo as mz
import pandas as pd
import numpy as np
import sys
import json
from flask import request, Blueprint, jsonify


predict_main = Blueprint('predict', __name__)
ROOT_PATH = sys.path[0] + '/'


@predict_main.route('/<string:model>', methods=['POST'])
def DSSM(model):
    request_data = json.loads(request.data.decode('utf-8'))
    q = request_data['text1']
    d = request_data['text2']
    train_id = request_data['train_id']
    df = pd.DataFrame(data={'text_left': [q],
                            'text_right': [d],
                            'label': [0]})
    preprocessor_suffix = '.' + model + '_preprocessor'
    preprocessor = mz.load_preprocessor(ROOT_PATH + 'matchzoo_temp_files/preprocessors/' + train_id + preprocessor_suffix)
    predict_pack = mz.pack(df)
    predict_pack_processed = preprocessor.transform(predict_pack)
    keras.backend.clear_session()

    model_suffix = '.' + model + '_model'
    model = mz.load_model(ROOT_PATH + 'matchzoo_temp_files/models/' + train_id + model_suffix)
    predict_score = float(model.predict(predict_pack_processed[:10].unpack()[0])[0][0])
    ret_dict = {
        'score': predict_score
    }
    '''
    if model != 'drmm':
        model_suffix = '.' + model + '_model'
        model = mz.load_model(ROOT_PATH + 'matchzoo_temp_files/models/' + train_id + model_suffix)
        predict_score = float(model.predict(predict_pack_processed[:10].unpack()[0])[0][0])
        ret_dict = {
            'score': predict_score
        }
    else:
        glove_embedding = mz.datasets.embeddings.load_glove_embedding(dimension=300)
        embedding_matrix = glove_embedding.build_matrix(preprocessor.context['vocab_unit'].state['term_index'])
        l2_norm = np.sqrt((embedding_matrix * embedding_matrix).sum(axis=1))
        embedding_matrix = embedding_matrix / l2_norm[:, np.newaxis]
        pred_generator = mz.HistogramDataGenerator(data_pack=predict_pack_processed,
                                                   embedding_matrix=embedding_matrix,
                                                   bin_size=30,
                                                   hist_mode='LCH')
        test_x, test_y = pred_generator[:]
        keras.backend.clear_session()
        model_suffix = '.' + model + '_model'
        model = mz.load_model(ROOT_PATH + 'matchzoo_temp_files/models/' + train_id + model_suffix)
        predict_score = float(model.predict(test_x)[0][0])
        ret_dict = {
            'score': predict_score
        }
    '''
    return jsonify(ret_dict)
