import webbrowser

import PySide6.QtWidgets
from PySide6.QtWidgets import QDialog, QPushButton
from PySide6.QtCore import Qt, Slot
from ..ui_forms.ui_DialogPluginInfo import Ui_Dialog
from .FailWidget import FailWidget

from .. parameters import *
from .. import lang_constants as lc
from .PMtypes import PluginListItem



class DialogPluginInfo(QDialog):
    """ Dialog for output plugin information located in <ub_info>"""

    def __init__(self, plugin:PluginListItem, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self._fill_form(plugin)

    def _fill_form(self, plugin:PluginListItem):
        info = plugin.module.ub_info
        self.ui.name_label.setText(plugin.plugin_name)

        labels = {"description": self.ui.description_label,
                  "author": self.ui.author_name_label,
                  "author_webpage": self.ui.author_url_btn,
                  "author_email": self.ui.author_email_btn,
                  "version": self.ui.version_label,
                  "wiki_url": self.ui.wiki_url_btn}


        for key in labels:
            if (key in info) and type(info[key]) is str:
                labels[key].setText(info[key])
            else:
                labels[key].setText(f"({lc.UNDEFINED})")
                if isinstance(labels[key], QPushButton):
                    labels[key].setEnabled(False)

        self.ui.author_url_btn.clicked.connect(lambda:self._open_url(self.ui.author_url_btn.text()))
        self.ui.author_email_btn.clicked.connect(lambda:self._open_url(self.ui.author_email_btn.text(), "email"))
        self.ui.wiki_url_btn.clicked.connect(lambda:self._open_url(self.ui.wiki_url_btn.text()))

    @Slot()
    def _open_url(self, url:str, mode:str = "site"):
        if mode == "site":
            webbrowser.open_new_tab(url)
        elif mode == "email":
            webbrowser.open(f"mailto:{url}")
