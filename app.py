import os
import sys
import json
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename

from utils import json_read, json_write, copy_file_to_destination
from train import main as train_request
from nlu_predict import predict_main as predict_request
from preprocess import main as preprocess_request
from tune import main as tune_request


app = Flask(__name__)

app.register_blueprint(train_request, url_prefix='/train')
app.register_blueprint(predict_request, url_prefix='/predict')
app.register_blueprint(preprocess_request, url_prefix='/preprocess')
app.register_blueprint(tune_request, url_prefix='/tune')


ROOT_PATH = sys.path[0] + '/'
ALLOWED_EXTENSIONS = set(['train', 'valid'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check')
def check():
    return 'pong'


@app.route('/files', methods=['POST'])
def get_files():
    if request.method == 'POST':
        file = request.files['train_file']
        filename = request.form['file_name']
        if allowed_file(filename):
            filename = secure_filename(filename)
            file.save(os.path.join(ROOT_PATH + 'matchzoo_temp_files/files', filename))
            return 'Receive File!'
    return 'Filter!'


@app.route('/get_jupyter', methods=['POST'])
def get_jupyter():
    request_data = json.loads(request.data.decode('utf-8'))
    guideline_id = request_data['guideline_id']
    model_name = request_data['model_name']
    from_path = ROOT_PATH + 'jupyters/' + model_name + '/sandbox.ipynb'
    to_path = ROOT_PATH + 'matchzoo_temp_files/jupyters/' + guideline_id + '.ipynb'
    copy_file_to_destination(from_path, to_path)
    ret_dict = {
        'jupyter_url': 'http://127.0.0.1:8999/notebooks/' + guideline_id + '.ipynb'
    }
    return jsonify(ret_dict)


if __name__ == '__main__':
    print(ROOT_PATH)
    app.run(host='0.0.0.0', port=9773, threaded=True)
