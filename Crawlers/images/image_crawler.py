from configparser import ConfigParser
import requests
import os
import shutil
from multiprocessing import Process
import numpy as np

CFG_PATH = './settings.cfg'

# section URL
SECTION_URL = 'URL'
URL_FORMAT = 'url.format'
PARAM_COUNT = 'url.param.count'
PARAM_KEY_START_FORMAT = 'url.param.{}.start'
PARAM_KEY_END_FORMAT = 'url.param.{}.end'
PARAM_KEY_DIGITS_FORMAT = 'url.param.{}.digits'
PARAM_KEY_LIST_FORMAT = 'url.param.{}.list'
PARAMS = 'params'

# section OUTPUT
SECTION_OUTPUT = 'OUTPUT'
OUTPUT_THREADS = 'output.threads'
OUTPUT_FOLDER_PATH = 'output.folder.path'
OUTPUT_FILE_EXTENSION = 'output.file.extension'
OUTPUT_FILE_FORMAT = 'output.file.format'
OUTPUT_FILE_REPLACE = 'output.file.replace'

def read_cfg():
    cfg = ConfigParser()
    cfg.read(CFG_PATH)

    dict_cfg = {
        URL_FORMAT: cfg[SECTION_URL][URL_FORMAT],
        PARAM_COUNT: int(cfg[SECTION_URL][PARAM_COUNT]),
        OUTPUT_FOLDER_PATH: cfg[SECTION_OUTPUT][OUTPUT_FOLDER_PATH],
        OUTPUT_FILE_EXTENSION: cfg[SECTION_OUTPUT][OUTPUT_FILE_EXTENSION],
        OUTPUT_FILE_FORMAT: cfg[SECTION_OUTPUT][OUTPUT_FILE_FORMAT],
        OUTPUT_THREADS: int(cfg[SECTION_OUTPUT].get(OUTPUT_THREADS, 2)),
        PARAMS: []
    }

    # preparing parameters
    for i in range(1, dict_cfg[PARAM_COUNT]+1):
        start_key = PARAM_KEY_START_FORMAT.format(i)
        end_key = PARAM_KEY_END_FORMAT.format(i)
        list_key = PARAM_KEY_LIST_FORMAT.format(i)
        zfill_key = PARAM_KEY_DIGITS_FORMAT.format(i)

        if cfg[SECTION_URL].get(start_key) != None \
                and cfg[SECTION_URL].get(end_key) != None:
            start = int(cfg[SECTION_URL][start_key])
            end = int(cfg[SECTION_URL][end_key])
            param_list = list(range(start, end+1))

            # zfill
            num_zfill = int(cfg[SECTION_URL].get(zfill_key, 0))
            if num_zfill != 0:
                for i in range(len(param_list)):
                    param_list[i] = str(param_list[i]).zfill(num_zfill)
        elif cfg[SECTION_URL].get(list_key) != None:
            param_list = list(cfg[SECTION_URL][list_key])

        dict_cfg[PARAMS].append(param_list)

    is_replace = cfg[SECTION_OUTPUT].get(OUTPUT_FILE_REPLACE)
    if is_replace != None:
        if is_replace.lower() == 'true':
            dict_cfg[OUTPUT_FILE_REPLACE] = True
        else:
            dict_cfg[OUTPUT_FILE_REPLACE] = False
    else:
        dict_cfg[OUTPUT_FILE_REPLACE] = False

    return dict_cfg

def prepare_params(cfg_param, count_params):
    queue = list()
    index = np.zeros(count_params, dtype=int)
    first_param_len = len(cfg_param[0])

    while index[0] < first_param_len:
        # append the params to queue
        params = list()
        for i, p in zip(index, cfg_param):
            params.append(p[i])
        queue.append(params)

        # move index
        index[-1] += 1
        for i in range(count_params-1, 0, -1):
            if index[i] >= len(cfg_param[i]):
                index[i] = index[i] - len(cfg_param[i])
                index[i-1] += 1

    return queue

def get_image(cfg, param):
    url = cfg[URL_FORMAT].format(*param)
    file_path = os.path.join(
            cfg[OUTPUT_FOLDER_PATH],
            cfg[OUTPUT_FILE_FORMAT].format(*param) + cfg[OUTPUT_FILE_EXTENSION]
    )

    # delete the file
    if cfg[OUTPUT_FILE_REPLACE]:
        os.remove(file_path)
    else:
        return None

    r = requests.get(url, stream=True)

    if r.status_code == 200:
        with open(file_path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        return True
    elif r.status_code == 404:
        return False
    else:
        return False

def get_images_task(cfg, queue):
    for param in queue:
        is_ok = get_image(cfg, param)

def main():
    cfg = read_cfg()
    print('Read config succeed.')

    if not os.path.exists(cfg[OUTPUT_FOLDER_PATH]):
        os.mkdir(cfg[OUTPUT_FOLDER_PATH])

    queue = prepare_params(cfg[PARAMS], cfg[PARAM_COUNT])
    print('Queue prepared. size:', len(queue))
    print('Start downloading with {} threads.'.format(cfg[OUTPUT_THREADS]))

    subqueue_size = int(len(queue) / cfg[OUTPUT_THREADS]) + 1
    for i in range(cfg[OUTPUT_THREADS]):
        subqueue = queue[subqueue_size*i: min(subqueue_size*(i+1), len(queue))]
        task = Process(target=get_images_task, args=(cfg, subqueue))
        task.start()

if __name__ == '__main__':
    main()
