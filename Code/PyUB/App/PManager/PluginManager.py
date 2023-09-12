
from ..UBoxSettings import UBoxSettings
from .FailWidget import FailWidget
from .PMtypes import PluginListItem, PluginParameters, PackageDirItem
from ... import utils
from ...Types.InputWidgets import CheckableButton
from ...Types import UBWidget
import os, sys, shelve, pickle, importlib, traceback, logging, time
from ..parameters import *
from .. import lang_constants as lc
from .DialogEditProperties import DialogEditProperties
from .DialogPluginInfo import DialogPluginInfo
from PySide6.QtCore import QObject, Qt
from PySide6.QtGui import QCursor, QStandardItemModel, QStandardItem, QColor
from PySide6.QtWidgets import QMainWindow, QTabWidget, QScrollArea, QWidget, QDialog, QSpacerItem, QHBoxLayout, QSizePolicy, QGridLayout, QLabel, QPushButton, QMenu, QApplication, QListView, QMessageBox
from PySide6.QtCore import Qt, Slot
from collections import OrderedDict
from typing import Iterator
from ..app_utils import *


class PluginManager(QObject):
    def __init__(self, parent:QMainWindow):
        super().__init__()
        self._parent = parent
        self._app_settings:UBoxSettings = parent._settings

    def init_plugins(self):
        if not hasattr(self, "plugins_loaded"):
            self.plugins_loaded = True
            self._plugins = OrderedDict()

        packagedir_list = [("", get_plugin_dir())]
        packagedir_list.extend(self._app_settings.get_property_value("external_plugin_dir"))

        for nickname, path in packagedir_list:
            for dir in os.listdir(path):
                package_key = str((nickname, dir))
                if (dir.lower() in FOLDER_NAMES_IGNORE_LIST) or package_key in self._plugins:
                    continue
                self._plugins[package_key] = PluginListItem()
                self._plugins[package_key].plugin_dirsite = path
                self._plugins[package_key].plugin_dir_name = dir

        self._load_plugins(list(self._plugins.keys()), clear_load=True)
        self._controlarea.setWidget(self._render_plugins_control_widget())
        self._on_tab_changed(0)

    def _load_plugins(self, key_list:list[str], reset_settings=False, clear_load=False):
        if len(key_list) == 0: return

        if clear_load:
            self._twidget.clear()

        cur_package_site = ""
        self._twidget.currentChanged.disconnect(self._on_tab_changed)

        with shelve.open(get_plugin_data_dir()) as data:
            for key in key_list:
                cur_plugin = self._plugins[key]
                cur_plugin.plugin_db_key = key
                cur_plugin.is_valid = True
                utils.ubwidgets_list.clear()

                if not clear_load:
                    tw = self._twidget
                    for i in range(tw.count()):
                        if isinstance(tw.widget(i), cur_plugin.ubwidget_class) or (isinstance(tw.widget(i), QWidget) and tw.widget(i).load_key == key):
                            tw.removeTab(i)

                if cur_package_site != cur_plugin.plugin_dirsite:
                    if cur_package_site in sys.path: sys.path.remove(cur_package_site)
                    cur_package_site = cur_plugin.plugin_dirsite
                    sys.path.append(cur_package_site)

                try:
                    if not cur_plugin.module:
                        cur_plugin.module = importlib.import_module(cur_plugin.plugin_dir_name)
                        self._add_log_message(lc.LOG_PACKAGE_HASBEEN_LOADED_SUCCESS.format(name=cur_plugin.module),None,"green")
                    else:
                        cur_plugin.module = importlib.reload(cur_plugin.module)
                        self._add_log_message(lc.LOG_PACKAGE_HASBEEN_RELOADED_SUCCESS.format(name=cur_plugin.module),None,"green")
                except Exception as exc:
                    package_dir = cur_plugin.plugin_dirsite
                    package_name = cur_plugin.plugin_dir_name
                    package_path = package_dir + os.sep + package_name
                    self._add_log_message(lc.LOG_PACKAGE_IMPORT_FAIL.format(path=package_path), traceback.format_exc(), "red")
                    if not cur_plugin.module:
                        del self._plugins[key]
                    continue

                if len(utils.ubwidgets_list) == 1 and issubclass(utils.ubwidgets_list[0], UBWidget):
                    cur_plugin.ubwidget_class = utils.ubwidgets_list[0]
                else:
                    cur_plugin.is_valid = False
                    continue

                try:
                    if key in data:
                        if hasattr(cur_plugin.ubwidget_class, "ub_settings"):
                            if reset_settings:
                                data_item:PluginParameters = data[key]
                                data_item.settings_params_dict = cur_plugin.ubwidget_class.ub_settings.prop_params_to_dict()
                                data_item.settings_prop_values = cur_plugin.ubwidget_class.ub_settings.propvalues_to_dict()
                                data[key] = data_item
                            else:
                                cur_plugin.ubwidget_class.ub_settings.set_prop_params_from_dict(data[key].settings_params_dict)
                                cur_plugin.ubwidget_class.ub_settings.set_propvalues_from_dict(data[key].settings_prop_values)
                        cur_plugin.is_enabled = data[key].enabled
                        cur_plugin.init_on_startup = data[key].init_on_startup
                    else:
                        pl_params = PluginParameters()
                        if hasattr(cur_plugin.ubwidget_class, "ub_settings"):
                            pl_params.settings_prop_values = cur_plugin.ubwidget_class.ub_settings.propvalues_to_dict()
                            pl_params.settings_params_dict = cur_plugin.ubwidget_class.ub_settings.prop_params_to_dict()
                        data[key] = pl_params
                except Exception as exc:
                    self._add_log_message(lc.LOG_SETTINGS_INIT_ERROR.format(module=cur_plugin.module),traceback.format_exc(),"red")
                    cur_plugin.is_valid = False
                    continue

                if hasattr(cur_plugin.ubwidget_class, "ub_name") and type(cur_plugin.ubwidget_class.ub_name) is str:
                    cur_plugin.plugin_name = cur_plugin.ubwidget_class.ub_name
                else:
                    cur_plugin.plugin_name = cur_plugin.plugin_dir_name
                cur_plugin.plugin_short_name = utils.crop_string(cur_plugin.plugin_name, 20)

                if cur_plugin.is_enabled:
                    if cur_plugin.init_on_startup:
                        try:
                            widget = cur_plugin.ubwidget_class()
                        except Exception as exc:
                            widget = FailWidget()
                            widget.set_error_msg(
                                lc.ERROR_WIDGET_INIT.format(wgt_class=cur_plugin.ubwidget_class,
                                                            traceback_info=traceback.format_exc()))
                        finally:
                            widget.load_key = key
                            self._twidget.addTab(widget, cur_plugin.plugin_short_name)

                    else:
                        dummy_widget = QWidget()
                        dummy_widget.load_key = key
                        self._twidget.addTab(dummy_widget, "*" + cur_plugin.plugin_short_name)

        sys.path.remove(cur_package_site)
        utils.ubwidgets_list.clear()
        self._twidget.currentChanged.connect(self._on_tab_changed)

    def _reload_plugin(self, plugin:PluginListItem):
        self._load_plugins([plugin.plugin_db_key], reset_settings=True)

    def _render_plugins_control_widget(self) -> QWidget:

        logging.debug("Creating plugin page")
        widget = QWidget()
        h_layout = QHBoxLayout(widget)
        nested_widget = QWidget()
        h_layout.addWidget(nested_widget)
        layout = QGridLayout(nested_widget)
        v_spacer = QSpacerItem(20, 40, QSizePolicy.Maximum, QSizePolicy.Expanding)
        h_spacer2 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Maximum)
        h_spacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Maximum)

        row_counter: int = 0
        plugins = self._plugins
        for i, key in enumerate(plugins.keys()):
            if not plugins[key].is_valid: continue
            row_counter = i
            label = QLabel()
            label.setText(plugins[key].plugin_short_name)
            if plugins[key].plugin_name != plugins[key].plugin_short_name:
                label.setToolTip(plugins[key].plugin_name)
            logging.debug(len(plugins[key].plugin_name))
            label.setWordWrap(False)
            layout.addWidget(label, i, 0, Qt.AlignRight)

            switch_btn = CheckableButton(state=plugins[key].is_enabled, enabled_text=lc.SWITCH_PLUGIN_BTN_ENABLED,
                                         disabled_text=lc.SWITCH_PLUGIN_BTN_DISABLED)
            switch_btn.state_changed.connect(self._on_activate_btn)
            switch_btn.plugin = self._plugins[key]
            layout.addWidget(switch_btn, i, 2, Qt.AlignCenter)

            config_btn = QPushButton(lc.CONFIGURATE)
            if hasattr(plugins[key].ubwidget_class, "ub_settings"):
                config_btn.clicked.connect(self._on_edit_prop_btn)
                config_btn.plugin = self._plugins[key]
                logging.debug(f"Attached property edit handler for class: {plugins[key].ubwidget_class.__name__}")
            else:
                config_btn.setEnabled(False)
            layout.addWidget(config_btn, i, 3, Qt.AlignCenter)

            extra_btn = QPushButton(u"…")
            extra_btn.plugin = self._plugins[key]
            extra_btn.clicked.connect(self._on_extra_btn)
            layout.addWidget(extra_btn, i, 4, Qt.AlignCenter)

        h_layout.addItem(h_spacer2)
        layout.addItem(v_spacer, row_counter + 1, 3)
        layout.addItem(h_spacer, 0, 1)
        return widget

    def _save_plugin_settings(self, plugin: PluginListItem):
        '''Save settings of plugin on HDD'''
        with shelve.open(get_plugin_data_dir()) as data:
            key = plugin.plugin_db_key
            if hasattr(plugin.ubwidget_class, "ub_settings"):
                logging.debug(f"Saving settings for plugin: {plugin.plugin_name}")
                temp = data[key]
                temp.settings_prop_values = plugin.ubwidget_class.ub_settings.propvalues_to_dict()
                data[key] = temp

    @Slot()
    def _on_extra_btn(self):
        '''Handle press on extra button on plugins page'''
        plugin = self.sender().plugin
        menu = QMenu(self._parent)
        menu.setFont(QApplication.font())

        def change_init_on_startup():
            nonlocal plugin
            plugin.init_on_startup = not plugin.init_on_startup

        def show_info():
            nonlocal plugin
            dialog = DialogPluginInfo(plugin, self._parent)
            # dialog.set_text(plugin.ubwidget_class.ub_description)
            dialog.exec()

        def reset_settings():
            nonlocal plugin
            answer = QMessageBox.question(self._parent, lc.RESET_SETTINGS, lc.QUESTION_RESET_SETTINGS)
            if answer:
                self._reload_plugin(plugin)


        show_description_action = menu.addAction(lc.INFO)
        if hasattr(plugin.module, "ub_info") and type(plugin.module.ub_info) is dict:
            show_description_action.triggered.connect(show_info)
        else:
            show_description_action.setEnabled(False)

        reset_settings_action = menu.addAction(lc.RESET_SETTINGS)
        if not hasattr(plugin.ubwidget_class, "ub_settings"):
            reset_settings_action.setEnabled(False)
        else:
            reset_settings_action.triggered.connect(reset_settings)

        init_in_startup_action = menu.addAction(lc.INIT_ON_STARTUP)
        init_in_startup_action.setCheckable(True)
        init_in_startup_action.setChecked(plugin.init_on_startup)
        init_in_startup_action.triggered.connect(change_init_on_startup)

        menu.popup(QCursor.pos())

    @Slot()
    def _on_edit_prop_btn(self):
        '''Handle press on "Configurate" button on plugins page'''
        plugin:PluginListItem = self.sender().plugin
        dialog = DialogEditProperties(self._parent, plugin)
        res = dialog.exec_()
        if res == QDialog.Accepted and not dialog.is_error_occured():
            if (plugin.ubwidget_class.ub_settings.update_data()):
                self._save_plugin_settings(plugin)
                for j in range(self._twidget.count()):
                    if type(self._twidget.widget(j)) is plugin.ubwidget_class:
                        try:
                            self._twidget.widget(j).settings_changed()
                        except Exception as exc:
                            key = self._twidget.widget(j).load_key
                            plugin_name = self._plugins[key].plugin_name
                            self._add_log_message(lc.LOG_SETTING_CHANGED_CALL_ERROR.format(plugin=plugin_name), traceback.format_exc(), "red")
                        break

    @Slot(bool)
    def _on_activate_btn(self, state: bool):
        '''Handle press on 2 state button on plugins page'''
        plugin: PluginListItem = self.sender().plugin
        plugin.is_enabled = state

    def update_plugins(self, update_tabs=False):
        """Save extra settings of plugins on HDD and refresh tabs"""
        with shelve.open(get_plugin_data_dir()) as data:
            for i, plugin in self._plugins.items():
                key = plugin.plugin_db_key
                temp_data = data[key]
                logging.debug \
                    (f"{plugin.ubwidget_class.__name__} activity, cur_value: {plugin.is_enabled}, stored value: {temp_data.enabled}")

                if temp_data.init_on_startup != plugin.init_on_startup:
                    temp_data.init_on_startup = plugin.init_on_startup
                    data[key] = temp_data

                if temp_data.enabled != plugin.is_enabled:
                    temp_data.enabled = plugin.is_enabled
                    data[key] = temp_data

                    if (not update_tabs): continue

                    if plugin.is_enabled:
                        pl_name = plugin.plugin_short_name
                        widget = plugin.ubwidget_class()
                        widget.load_key = key
                        self._twidget.addTab(widget, pl_name)
                    else:
                        for j in range(self._twidget.count()):
                            widget = self._twidget.widget(j)
                            if widget.load_key == key:
                                self._twidget.removeTab(j)
                                break

    def reload_plugins(self):
        self.update_plugins(update_tabs=False)
        self.init_plugins()

    @Slot(int)
    def _on_tab_changed(self, index:int):
        cur_widget = self._twidget.widget(index)
        if type(cur_widget) is QWidget:
            key = cur_widget.load_key
            self._twidget.currentChanged.disconnect(self._on_tab_changed)
            try:
                new_widget = self._plugins[key].ubwidget_class()
            except Exception as exc:
                # pass
                new_widget = FailWidget()
                new_widget.set_error_msg(lc.ERROR_WIDGET_INIT.format(wgt_class=self._plugins[key].ubwidget_class, traceback_info=traceback.format_exc()))
            finally:
                self._twidget.removeTab(index)
                new_widget.load_key = key
                self._twidget.insertTab(index, new_widget, self._plugins[key].plugin_short_name)
                self._twidget.setCurrentIndex(index)
            self._twidget.currentChanged.connect(self._on_tab_changed)

    def set_qtabwidget(self, twidget:QTabWidget):
        self._twidget:QTabWidget = twidget
        twidget.currentChanged.connect(self._on_tab_changed)

    def set_controlarea(self, scroll_area:QScrollArea):
        self._controlarea = scroll_area

    def set_log_view(self, list_view:QListView):
        self._log_model = QStandardItemModel()
        self._log_listview = list_view
        self._log_listview.setModel(self._log_model)


    def _add_log_message(self, msg:str, trace:str="", color:str = "none")->None:
        strtime = time.strftime("%H:%M:%S", time.localtime())
        is_show_error_info = self._app_settings.get_property_value("show_error_msg")

        if trace and is_show_error_info:
            text = f"{strtime}⮞ {msg}\n\n{trace}"
        else:
            text = f"{strtime}⮞ {msg}"

        item = QStandardItem(text)
        match color:
            case "red": item.setBackground(QColor(255, 140, 140))
            case "yellow": item.setBackground(QColor(250, 237, 105))
            case "green": item.setBackground(QColor(142, 255, 140))
        item.setFont(QApplication.font())
        self._log_model.insertRow(0, item)
