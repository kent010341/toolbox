from configparser import ConfigParser

CFG_PATH = './settings.cfg'

# section URL
SECTION_URL = 'URL'
URL_FORMAT = 'url.format'
PARAM_COUNT = 'url.param.count'
PARAM_KEY_START_FORMAT = 'url.param.{}.start'
PARAM_KEY_END_FORMAT = 'url.param.{}.end'
PARAM_KEY_LIST_FORMAT = 'url.param.{}.list'

# section OUTPUT
SECTION_OUTPUT = 'OUTPUT'
OUTPUT_FOLDER_PATH = 'output.folder.path'
OUTPUT_EXTENSION = 'output.extension'
OUTPUT_FORMAT = 'output.format'

# section HTML
SECTION_HTML = 'HTML'
HTML_IMG_PREFIX = 'html.img.prefix'
HTML_IMG_SUFFIX = 'html.img.suffix'
HTML_NOTFOUND_PREFIX = 'html.notfound.prefix'
HTML_NOTFOUND_SUFFIX = 'html.notfound.suffix'

def read_cfg():
    cfg = ConfigParser()
    cfg.read(CFG_PATH)

    dict_cfg = {
        URL_FORMAT: cfg[SECTION_URL][URL_FORMAT],
        PARAM_COUNT: int(cfg[SECTION_URL][PARAM_COUNT]),
        OUTPUT_FOLDER_PATH: cfg[SECTION_OUTPUT][OUTPUT_FOLDER_PATH],
        OUTPUT_EXTENSION: cfg[SECTION_OUTPUT][OUTPUT_EXTENSION],
        OUTPUT_FORMAT: cfg[SECTION_OUTPUT][OUTPUT_FORMAT],
        HTML_IMG_PREFIX: cfg[SECTION_HTML][HTML_IMG_PREFIX],
        HTML_IMG_SUFFIX: cfg[SECTION_HTML][HTML_IMG_SUFFIX],
        HTML_NOTFOUND_PREFIX: cfg[SECTION_HTML][HTML_NOTFOUND_PREFIX],
        HTML_NOTFOUND_SUFFIX: cfg[SECTION_HTML][HTML_NOTFOUND_SUFFIX],
        'params': []
    }

    for i in range(1, dict_cfg[PARAM_COUNT]+1):
        start_key = PARAM_KEY_START_FORMAT.format(i)
        end_key = PARAM_KEY_END_FORMAT.format(i)
        list_key = PARAM_KEY_LIST_FORMAT.format(i)

        if cfg[SECTION_URL].get(start_key) != None \
                and cfg[SECTION_URL].get(end_key) != None:
            start = int(cfg[SECTION_URL][start_key])
            end = int(cfg[SECTION_URL][end_key])
            param_list = list(range(start, end+1))
        elif cfg[SECTION_URL].get(list_key) != None:
            param_list = list(cfg[SECTION_URL][list_key])

        dict_cfg['params'].append(param_list)

    return dict_cfg

def prepare_params(cfg_param):
    pass

def main():
    cfg = read_cfg()

if __name__ == '__main__':
    main()
