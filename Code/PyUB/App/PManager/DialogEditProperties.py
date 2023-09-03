import sys, os, logging, math, traceback

import PySide6.QtWidgets
from PySide6.QtWidgets import QDialog
from ..ui_forms import Ui_Dialog
from .FailWidget import FailWidget

from .. parameters import *
from .. import lang_constants as lc
from .PMtypes import PluginListItem

logging.basicConfig(level=logging.DEBUG)
if(LOGGING_DISABLED):
    logging.disable(logging.CRITICAL)


class DialogEditProperties(QDialog):
    """ Dialog window for values editing in PropertyContainer"""

    def __init__(self, parent, item: PluginListItem):
        super().__init__()
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)
        self._ui.frameLangSelect.setVisible(False)
        self._error_occured = False

        self._item = item

        if parent.windowIcon():
            self.setWindowIcon(parent.windowIcon())
        try:
            self._ui.widget_place.addWidget(item.ubwidget_class.ub_settings.render_layout())
            self.retranslate()
        except Exception:
            fail_widget = FailWidget()
            fail_widget.set_error_msg(lc.ERROR_SETTING_RENDER_LAYOUT.format(pc_class=item.ubwidget_class.ub_settings, traceback_info=traceback.format_exc()))
            self._ui.widget_place.addWidget(fail_widget)
            self.retranslate(error_occured=True)
            self._error_occured = True

        screen = PySide6.QtWidgets.QApplication.primaryScreen()
        width = screen.availableSize().width() * 0.8
        height = math.trunc(screen.availableSize().height() * .8)
        self.resize(width, height)

    def is_error_occured(self):
        return self._error_occured

    def retranslate(self, error_occured:bool = False) -> None:
        self._ui.retranslateUi(self)
        self.setWindowTitle(lc.DIALOG_TITLE_CONFIG_PLUGIN.format(self._item.plugin_name))
        if not error_occured:
            self._item.ubwidget_class.ub_settings.retranslate()


#





