
from . import parameters
import os


def get_plugin_data_dir() -> str:
    home_dir = parameters.HOME_DIR
    return home_dir + os.sep + parameters.PLUGINS_DATA_PATH

def get_app_data_dir() -> str:
    home_dir = parameters.HOME_DIR
    return home_dir + os.sep + parameters.APP_DATA_PATH

def get_plugin_dir() -> str:
    home_dir = parameters.HOME_DIR
    return home_dir + os.sep + parameters.PLUGIN_DIR_PATH
