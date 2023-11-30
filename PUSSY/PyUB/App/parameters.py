

LOGGING_DISABLED = 1

VERSION = (0, 2, 0)

FOLDER_NAMES_IGNORE_LIST = {"template"}

HOME_DIR = ""
PLUGINS_DATA_PATH = r"data/plugins/plugins_data"
PLUGINS_LOCALSTORAGE_PATH = r"data/localstorage"
APP_DATA_PATH = r"data/app/app_data"
PLUGIN_DIR_PATH = r"Plugins"


import logging

if LOGGING_DISABLED:
    logging.basicConfig(level=logging.CRITICAL)
else:
    logging.basicConfig(level=logging.DEBUG)