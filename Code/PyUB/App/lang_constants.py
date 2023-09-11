
from PySide6.QtCore import QCoreApplication

CONFIGURATE = QCoreApplication.translate("mainwindow", "Configurate")
SWITCH_PLUGIN_BTN_ENABLED = QCoreApplication.translate("mainwindow", "Enabled")
SWITCH_PLUGIN_BTN_DISABLED = QCoreApplication.translate("mainwindow", "Disabled")

DIALOG_TITLE_CONFIG_PLUGIN = QCoreApplication.translate("dialog", "Configurate plugin: {0}")
DIALOG_TITLE_WARNING = QCoreApplication.translate("dialog", "Warning")
DIALOG_PB_TITLE_LOAD_PLUGINS = QCoreApplication.translate("dialog", "Plugins Loading")
DIALOG_APPLY_AFTER_RESTART = QCoreApplication.translate("dialog", "Some setting will be applied only after restart")

ERROR_WIDGET_INIT = QCoreApplication.translate("errors", "Widget initialization error ({wgt_class}) \n\n[Traceback info:]\n{traceback_info}")
ERROR_SETTING_RENDER_LAYOUT = QCoreApplication.translate("errors", "Settings layout rendering error ({pc_class}) \n\n[Traceback info:]\n{traceback_info}")

OPEN_MANUAL = QCoreApplication.translate("mainwindow", "Open user manual")
INIT_ON_STARTUP = QCoreApplication.translate("mainwindow", "Initialize on startup")
INFO = QCoreApplication.translate("mainwindow", "Info")
RESET_SETTINGS = QCoreApplication.translate("mainwindow", "Reset plugin settings")

LOG_PACKAGE_HASBEEN_LOADED_SUCCESS = QCoreApplication.translate("Logs", "Package ({name}) has been imported successfully")
LOG_PACKAGE_HASBEEN_RELOADED_SUCCESS = QCoreApplication.translate("Logs", "Package ({name}) has been reloaded successfully")
LOG_PACKAGE_IMPORT_FAIL = QCoreApplication.translate("Logs", "Package from ({path}) importing has been failed")