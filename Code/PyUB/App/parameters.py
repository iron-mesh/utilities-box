

LOGGING_DISABLED = 0

VERSION = (0, 0, 1, "dev")

FOLDER_NAMES_IGNORE_LIST = {"template"}

HOME_DIR = ""
PLUGINS_DATA_PATH = r"data/plugins/plugins_data"
APP_DATA_PATH = r"data/app/app_data"
PLUGIN_DIR_PATH = r"Plugins"


import logging

if LOGGING_DISABLED:
    logging.basicConfig(level=logging.CRITICAL)
else:
    logging.basicConfig(level=logging.DEBUG)