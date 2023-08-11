
from PySide6.QtCore import QCoreApplication

CONFIGURATE = QCoreApplication.translate("mainwindow", "Configurate")
SWITCH_PLUGIN_BTN_ENABLED = QCoreApplication.translate("mainwindow", "Enabled")
SWITCH_PLUGIN_BTN_DISABLED = QCoreApplication.translate("mainwindow", "Disabled")

DIALOG_TITLE_CONFIG_PLUGIN = QCoreApplication.translate("dialog", "Configurate plugin: {0}")
DIALOG_PB_TITLE_LOAD_PLUGINS = QCoreApplication.translate("dialog", "Plugins Loading")

ERROR_WIDGET_INIT = QCoreApplication.translate("errors", "Widget initialization error ({wgt_class}) \n\n[Traceback info:]\n{traceback_info}")
ERROR_SETTING_RENDER_LAYOUT = QCoreApplication.translate("errors", "Settings layout rendering error ({pc_class}) \n\n[Traceback info:]\n{traceback_info}")