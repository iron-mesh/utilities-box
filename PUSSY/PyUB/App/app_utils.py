
from . import parameters
import os, importlib, types


def get_plugin_data_dir() -> str:
    home_dir = parameters.HOME_DIR
    return home_dir + os.sep + parameters.PLUGINS_DATA_PATH

def get_app_data_dir() -> str:
    home_dir = parameters.HOME_DIR
    return home_dir + os.sep + parameters.APP_DATA_PATH

def get_plugin_dir() -> str:
    home_dir = parameters.HOME_DIR
    return home_dir + os.sep + parameters.PLUGIN_DIR_PATH

def is_valid_package(path:str)->bool:
    """Check file|dir is python package"""
    return os.path.exists(path) and os.path.isdir(path) and "__init__.py" in [e for e in os.listdir(path) if os.path.isfile(path + os.sep + e)]

def rreload(module):
    """Recursively reload modules."""
    importlib.reload(module)
    print(module)
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if type(attribute) is types.ModuleType:
            rreload(attribute)



