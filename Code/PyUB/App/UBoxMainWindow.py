
from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout, QHBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy, QDialog, QApplication
from PySide6.QtCore import Qt, Slot, QCoreApplication
from PySide6.QtGui import QFont

from .UBoxSettings import UBoxSettings
from .ui_forms import Ui_MainWindow
from .app_types import  AppDataKeys
import os, sys, shelve, pickle
from .constants import *
from . import lang_constants as lc
from .PManager import PluginManager

import logging, importlib, traceback

logging.basicConfig(level=logging.DEBUG)
if LOGGING_DISABLED:
    logging.disable(level=logging.CRITICAL)

class UBoxMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #settings loading
        self._settings = UBoxSettings
        self._load_app_settings()

        self._init_gui_elements()
        # plugins loading
        self.plugin_manager = PluginManager(self)
        self.plugin_manager.set_qtabwidget(self.ui.tabWidgetPlugins)
        self.plugin_manager.set_controlarea(self.ui.scrollAreaPlugins)

        self._init_link_handlers()

        self.st_widget_page = self.ui.stackedWidget.currentIndex()

    def _init_link_handlers(self):
        self.ui.menu_settings.triggered.connect(lambda:self.change_page(2))
        self.ui.menu_plugins.triggered.connect(lambda:self.change_page(1))
        self.ui.menu_logs.triggered.connect(lambda:self.change_page(3))
        self.ui.menu_exit.triggered.connect(self.close)
        self.ui.btnReloadPlugins.clicked.connect(self._on_reload_plugins)
        self.ui.pushButtonClosePluginPage.clicked.connect(self._back_to_mainpage)
        self.ui.pushButtonCloseSettingsPage.clicked.connect(self._back_to_mainpage)
        self.ui.pushButtonCloseLogs.clicked.connect(self._back_to_mainpage)
        self.ui.stackedWidget.currentChanged.connect(self._on_stacked_widget_current_changed)
        self.ui.pushButtonAplySettings.clicked.connect(self._save_app_settings)

    def _init_gui_elements(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.tabWidgetPlugins.clear()
        self.ui.widget_place.addWidget(self._settings.render_layout())

    def change_page(self, index:int) -> None:
        self.ui.stackedWidget.setCurrentIndex(index)

    def _on_menu_about(self):
        pass

    def _on_menu_help(self):
        pass

    def _back_to_mainpage(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def show(self) -> None:
        super().show()
        self.plugin_manager.load_plugins()

    def _on_reload_plugins(self):
        self.plugin_manager.update_plugins(update_tabs=False)
        self.plugin_manager.load_plugins()

    @Slot(int)
    def _on_stacked_widget_current_changed(self, index: int):
        logging.debug(index)
        if self.st_widget_page == 1: #plugins
            self.plugin_manager.update_plugins(update_tabs=True)
        elif self.st_widget_page == 2: #app settings
            pass
        self.st_widget_page = self.ui.stackedWidget.currentIndex()

    def _load_app_settings(self):
        with shelve.open(APP_DATA_PATH) as data:
            key = AppDataKeys.SettingsDict
            if key in data:
                self._settings.set_propvalues_from_dict(data[key])
            else:
                data[key] = self._settings.propvalues_to_dict()
        self._apply_settings()

    @Slot()
    def _save_app_settings(self) -> None:
        if self._settings.update_data():
            with shelve.open(APP_DATA_PATH) as data:
                data[AppDataKeys.SettingsDict] = self._settings.propvalues_to_dict()
            self._apply_settings()

    def _apply_settings(self):
        app = QApplication.instance()
        font_size = self._settings.get_property_value("font_size")
        font_family = self._settings.get_property("font_family").get_current_font().family()
        app.setFont(QFont(font_family, font_size, QFont.Normal))
        app.setStyle(self._settings.get_property("style").get_current_item_text())