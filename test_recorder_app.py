from aip import AipSpeech

ROOT_PATH = './'

def recorder():
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    APP_ID = '15350677'
    API_KEY = 'fQjZY818Q8dMY7jQ22lrjPVh'
    SECRET_KEY = 'QkL19cWgOjCgRxm7k235lxIetCBoaCib'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    print('start read')
    f = get_file_content(ROOT_PATH + 'matchzoo_temp_files/recorder/test.pcm')
    print('end read')
    r = client.asr(f, 'pcm', 16000, {
        'dev_pid': 1536,
    })
    print(r)


if __name__ == '__main__':
    recorder()
