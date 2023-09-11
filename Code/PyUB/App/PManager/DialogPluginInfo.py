import sys, os, logging, math, traceback

import PySide6.QtWidgets
from PySide6.QtWidgets import QDialog, QVBoxLayout, QPlainTextEdit, QDialogButtonBox
from PySide6.QtCore import Qt
from ..ui_forms import Ui_Dialog
from .FailWidget import FailWidget

from .. parameters import *
from .. import lang_constants as lc
from .PMtypes import PluginListItem

logging.basicConfig(level=logging.DEBUG)
if(LOGGING_DISABLED):
    logging.disable(logging.CRITICAL)


class DialogPluginInfo(QDialog):
    """ Dialog window for values editing in PropertyContainer"""

    def __init__(self, parent):
        super().__init__()
        layout = QVBoxLayout(self)

        self.plain_text_edit =QPlainTextEdit()
        self.plain_text_edit.setReadOnly(True)
        layout.addWidget(self.plain_text_edit)

        buttonBox = QDialogButtonBox()
        buttonBox.setCenterButtons(True)
        buttonBox.setOrientation(Qt.Horizontal)
        buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        layout.addWidget(buttonBox)

        screen = PySide6.QtWidgets.QApplication.primaryScreen()
        width = screen.availableSize().width() if screen.availableSize().width() < 800 else 800
        height = math.trunc(screen.availableSize().height() * .8)
        self.resize(width, height)

    def set_text(self, text:str):
        self.plain_text_edit.setPlainText(text)





