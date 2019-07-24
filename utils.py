import json
import sys
import pandas as pd
import matchzoo as mz
from pathlib import Path


ROOT_PATH = sys.path[0] + '/'


def json_read(file_name):
    with open(file_name) as f:
        return json.loads(f.read())


def json_write(file_name, dictionary):
    with open(file_name, 'w') as f:
        f.write(json.dumps(dictionary, indent=2))


class IOpool(object):
    def __init__(self):
        self.train_id = ''

    def write(self, content):
        if content.find('/step') != -1:
            with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + self.train_id + '.log', 'a') as f:
                f.write(content)
        elif content.find('Validation:') != -1:
            with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + self.train_id + '.log', 'a') as f:
                f.write(content + '\n')

    def flush(self):
        pass

    def set_trainid(self, train_id):
        self.train_id = train_id


class LogDir(object):
    def __init__(self):
        self.preprocess_id = ''

    def write(self, content):
        with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + self.preprocess_id + '.preprocess_log', 'a') as f:
            f.write(content)

    def flush(self):
        pass

    def set_preprocess_id(self, preprocess_id):
        self.preprocess_id = preprocess_id


def format_stringio_to_json(train_id, file_name, epoch=30):
    result_dict = {
        'state': 'run',
        'data': {
            'loss': [[]],
            'accuracy': [[], [], []]
        }
    }
    with open(ROOT_PATH + 'matchzoo_temp_files/logger/' + train_id + '.log') as f:
        lines = f.readlines()
        line_cnt = int(len(lines) / 2)
        for idx in range(line_cnt):
            loss_line = lines[2 * idx]
            accuracy_line = lines[2 * idx + 1]
            loss_value = float(loss_line.split('loss: ')[1])
            ndc3 = float(accuracy_line.split('normalized_discounted_cumulative_gain@3(0.0): ')[1].split(' - ')[0])
            ndc5 = float(accuracy_line.split('normalized_discounted_cumulative_gain@5(0.0): ')[1].split(' - ')[0])
            mae = float(accuracy_line.split('mean_average_precision(0.0): ')[1])
            result_dict['data']['loss'][0].append({
                'x': idx + 1,
                'y': loss_value
            })
            result_dict['data']['accuracy'][0].append({
                'x': idx + 1,
                'y': mae
            })
            result_dict['data']['accuracy'][1].append({
                'x': idx + 1,
                'y': ndc3
            })
            result_dict['data']['accuracy'][2].append({
                'x': idx + 1,
                'y': ndc5
            })
    if len(result_dict['data']['loss'][0]) == epoch:
        result_dict['state'] = 'end'
    json_write(file_name, result_dict)
    # print()


def convert_to_right_type(obj_str):
    def isfloat(par):
        if par.find('.') == -1:
            return False
        part1, part2 = par.split('.')
        if part1.isdigit() and part2.isdigit():
            return True
        else:
            return False
    if obj_str.isdigit():
        return int(obj_str)
    elif isfloat(obj_str):
        return float(obj_str)
    else:
        return obj_str


def _load_data(task, path):
    if task == 'ranking':
        task = mz.tasks.Ranking()
    if task == 'classification':
        task = mz.tasks.Classification()
    data_pack = mz.pack(pd.read_csv(path, index_col=0, engine='python'))
    if isinstance(task, mz.tasks.Ranking):
        data_pack.relation['label'] = data_pack.relation['label'].astype('float32')
        return data_pack
    elif isinstance(task, mz.tasks.Classification):
        data_pack.relation['label'] = data_pack.relation['label'].astype(int)
        return data_pack.one_hot_encode_label(num_classes=2), [False, True]


def load_train_data(train_id, existing_dataset, task):
    if existing_dataset == '$None$':
        path = Path(__file__).parent.joinpath('matchzoo_temp_files/files/' + train_id + '.train')
        return _load_data(task, path=path)
    elif existing_dataset == 'Toy':
        return mz.datasets.toy.load_data('train', task=task)
    elif existing_dataset == 'WikiQA':
        return mz.datasets.wiki_qa.load_data('train', task=task)
    elif existing_dataset == 'SNLI':
        return mz.datasets.snli.load_data('train', task=task, target_label='entailment')


def load_test_data(test_id, existing_dataset, task):
    if existing_dataset == '$None$':
        path = Path(__file__).parent.joinpath('matchzoo_temp_files/files/' + test_id + '.valid')
        return _load_data(task, path=path)
    elif existing_dataset == 'Toy':
        return mz.datasets.toy.load_data('test', task=task)
    elif existing_dataset == 'WikiQA':
        return mz.datasets.wiki_qa.load_data('test', task='ranking', filtered=True)
    elif existing_dataset == 'SNLI':
        return mz.datasets.snli.load_data('test', task=task, target_label='entailment')


def copy_file_to_destination(path1, path2):
    with open(path1, encoding='utf-8') as f1:
        f2 = open(path2, 'w', encoding='utf-8')
        f2.write(f1.read())
        f2.close()


if __name__ == '__main__':
    path1 = './jupyters/dssm/sandbox.ipynb'
    path2 = './matchzoo_temp_files/jupyters/casualname.ipynb'
    copy_file_to_destination(path1, path2)
