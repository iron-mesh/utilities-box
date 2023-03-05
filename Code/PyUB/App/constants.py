
import os

LOGGING_DISABLED = not True

VERSION = (0,0,0)

APP_SETTINGS_KEY = "utilities_box"
FOLDER_NAMES_IGNORE_LIST = {APP_SETTINGS_KEY, "Template", "template"}
DATA_APP_PATH = "app_data" + os.sep + "data"
DATA_PLUGINS_PATH = "app_data" + os.sep + "plugins_data"