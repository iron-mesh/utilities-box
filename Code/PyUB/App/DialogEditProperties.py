import sys, os, logging, math

import PySide2.QtWidgets
from PySide2.QtWidgets import QDialog
from .ui_forms import Ui_Dialog

from . constants import *
from . import lang_constants as lc
from .types import PluginListItem

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

        self._item = item

        if parent.windowIcon():
            self.setWindowIcon(parent.windowIcon())

        # self._ui.widget = item.ubwidget_class.ub_settings.render_layout()
        self._ui.widget_place.addWidget(item.ubwidget_class.ub_settings.render_layout())
        self.retranslate()

        screen = PySide2.QtWidgets.QApplication.primaryScreen()
        width = screen.availableSize().width() if screen.availableSize().width() < 800 else 800
        height = math.trunc(screen.availableSize().height() * .8)
        self.resize(width, height)

    def retranslate(self) -> None:
        self._ui.retranslateUi(self)
        self.setWindowTitle(lc.DIALOG_TITLE_CONFIG_PLUGIN.format(self._item.plugin_name))
        self._item.ubwidget_class.ub_settings.retranslate()

    def update_data(self)->None:
        pass








