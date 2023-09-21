
from PySide6.QtCore import QCoreApplication

UNDEFINED = QCoreApplication.translate("dialog", "Undefined")

CONFIGURATE = QCoreApplication.translate("mainwindow", "Configurate")
SWITCH_PLUGIN_BTN_ENABLED = QCoreApplication.translate("mainwindow", "Enabled")
SWITCH_PLUGIN_BTN_DISABLED = QCoreApplication.translate("mainwindow", "Disabled")

DIALOG_TITLE_CONFIG_PLUGIN = QCoreApplication.translate("dialog", "Configurate plugin: {0}")
DIALOG_TITLE_DEL_INVALID_DATA = QCoreApplication.translate("dialog", "Delete invalid data?")
DIALOG_TITLE_WARNING = QCoreApplication.translate("dialog", "Warning")
DIALOG_TITLE_NOTIFICATION = QCoreApplication.translate("dialog", "Notification")
DIALOG_PB_TITLE_LOAD_PLUGINS = QCoreApplication.translate("dialog", "Plugins Loading")
DIALOG_RELOAD_PLUGINS = QCoreApplication.translate("dialog", "Reload plugins")
DIALOG_APPLY_AFTER_RESTART = QCoreApplication.translate("dialog", "Some setting will be applied only after restart")
DIALOG_MSG_APP_CLOSING_ERROR = QCoreApplication.translate("dialog", "An error occured when calling app_closing() method for [{cls}]\n{trace}")
DIALOG_INVALID_DATA_NOTFOUND = QCoreApplication.translate("dialog", "Invalid data hasn't been found.")
QUESTION_RESET_SETTINGS = QCoreApplication.translate("dialog", "Current setting will be erased. Proceed?")
QUESTION_RELOAD_PLUGINS = QCoreApplication.translate("dialog", "All plugins will be reloaded. Unsaved data will be erased. Proceed?")
QUESTION_DEL_INVALID_DATA = QCoreApplication.translate("dialog", "{count} records have been found. They will be erased permanently. Proceed?")

ERROR_WIDGET_INIT = QCoreApplication.translate("errors", "Widget initialization error ({wgt_class}) \n\n[Traceback info:]\n{traceback_info}")
ERROR_SETTING_RENDER_LAYOUT = QCoreApplication.translate("errors", "Settings layout rendering error ({pc_class}) \n\n[Traceback info:]\n{traceback_info}")


OPEN_MANUAL = QCoreApplication.translate("mainwindow", "Open user manual")
INIT_ON_STARTUP = QCoreApplication.translate("mainwindow", "Initialize on startup")
INFO = QCoreApplication.translate("mainwindow", "Info")
RESET_SETTINGS = QCoreApplication.translate("mainwindow", "Reset plugin settings")
INFO = QCoreApplication.translate("mainwindow", "Plugin info")
RESET_SETTINGS = QCoreApplication.translate("mainwindow", "Reset settings")

LOG_PACKAGE_HASBEEN_LOADED_SUCCESS = QCoreApplication.translate("Logs", "Package ({name}) has been imported successfully")
LOG_PACKAGE_HASBEEN_RELOADED_SUCCESS = QCoreApplication.translate("Logs", "Package ({name}) has been reloaded successfully")
LOG_PACKAGE_IMPORT_FAIL = QCoreApplication.translate("Logs", "Package from ({path}) importing has been failed!")
LOG_SETTINGS_INIT_ERROR = QCoreApplication.translate("Logs", "Initialization of settings for ({module}) has been failed!")
LOG_SETTINGS_SAVE_ERROR = QCoreApplication.translate("Logs", "Saving of settings for ({module}) has been failed!")
LOG_RESET_SETTINGS_ERROR = QCoreApplication.translate("Logs", "An error occurred when resetting the settings for ({module})")
LOG_SETTING_CHANGED_CALL_ERROR = QCoreApplication.translate("Logs", "When calling the method settings_changed() for plugin [{plugin}] an error occurred!")
LOG_SETTINGS_EDIT_STARTED_CALL_ERROR = QCoreApplication.translate("Logs", "When calling the method settings_edit_started() for plugin [{plugin}] an error occurred!")
LOG_SETTINGS_EDIT_FINISHED_CALL_ERROR = QCoreApplication.translate("Logs", "When calling the method settings_edit_finished() for plugin [{plugin}] an error occurred!")
LOG_DEACTIVATED_CALL_ERROR = QCoreApplication.translate("Logs", "When calling the method deactivated() for plugin [{plugin}] an error occurred!")