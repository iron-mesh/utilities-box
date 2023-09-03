
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
from .DialogShowDescription import DialogShowDescription
from PySide6.QtCore import QObject, Qt
from PySide6.QtGui import QCursor, QStandardItemModel, QStandardItem, QColor
from PySide6.QtWidgets import QMainWindow, QTabWidget, QScrollArea, QWidget, QDialog, QSpacerItem, QHBoxLayout, QSizePolicy, QGridLayout, QLabel, QPushButton, QMenu, QApplication, QListView
from PySide6.QtCore import Qt, Slot


class PluginManager(QObject):
    def __init__(self, parent:QMainWindow):
        super().__init__()
        self._parent = parent
        self._app_settings:UBoxSettings = parent._settings

    def load_plugins(self):
        packagedir_list =[PackageDirItem("", path:=os.path.abspath(r"Plugins"), os.listdir(path))]
        for nickname, path in self._app_settings.get_property_value("external_plugin_dir"):
            if not os.path.exists(path) or not os.listdir(path): continue
            packagedir_list.append(PackageDirItem(nickname, path, os.listdir(path)))

        self._twidget.currentChanged.disconnect(self._on_tab_changed)

        if not hasattr(self, "plugins_loaded"):
            self.plugins_loaded = True
            self._plugins = dict()

        self._twidget.clear()

        with shelve.open(PLUGINS_DATA_PATH) as data:

            for i in packagedir_list:
                sys.path.append(i.dir_abspath)

                for package in i.package_list:
                    package_key = str((i.dir_nickname, package))

                    if (package.lower() in FOLDER_NAMES_IGNORE_LIST):
                        continue
                    utils.ubwidgets_list.clear()

                    if (package_key not in self._plugins):
                        self._plugins[package_key] = PluginListItem()
                    try:
                        if not self._plugins[package_key].module:
                            self._plugins[package_key].module = importlib.import_module(package)
                            self._add_log_message(lc.LOG_PACKAGE_HASBEEN_LOADED_SUCCESS.format(name=self._plugins[package_key].module),"green")
                        else:
                            self._plugins[package_key].module = importlib.reload(self._plugins[package_key].module)
                            self._add_log_message(lc.LOG_PACKAGE_HASBEEN_RELOADED_SUCCESS.format(name=self._plugins[package_key].module),"green")
                    except Exception:
                        del self._plugins[package_key]
                        package_path = i.dir_abspath + os.sep + package
                        self._add_log_message(lc.LOG_PACKAGE_IMPORT_FAIL.format(path=package_path), "red")
                        continue

                    if len(utils.ubwidgets_list) == 1 and issubclass(utils.ubwidgets_list[0], UBWidget):
                        self._plugins[package_key].plugin_dir = package
                        self._plugins[package_key].plugin_db_key = package_key
                        self._plugins[package_key].plugin_absdirpath = i.dir_abspath + os.sep + package
                        self._plugins[package_key].ubwidget_class = utils.ubwidgets_list[0]
                    else:
                        del self._plugins[package_key]
                        continue

                    if package_key in data:
                        if hasattr(self._plugins[package_key].ubwidget_class, "ub_settings"):
                            self._plugins[package_key].ubwidget_class.ub_settings.set_prop_params_from_dict(data[package_key].settings_params_dict)
                            self._plugins[package_key].ubwidget_class.ub_settings.set_propvalues_from_dict(data[package_key].settings_prop_values)
                        self._plugins[package_key].is_enabled = data[package_key].enabled
                        self._plugins[package_key].init_on_startup = data[package_key].init_on_startup
                    else:
                        pl_params = PluginParameters()
                        if hasattr(self._plugins[package_key].ubwidget_class, "ub_settings"):
                            pl_params.settings_prop_values = self._plugins[package_key].ubwidget_class.ub_settings.propvalues_to_dict()
                            pl_params.settings_params_dict = self._plugins[package_key].ubwidget_class.ub_settings.prop_params_to_dict()
                        data[package_key] = pl_params

                    self._plugins[package_key].plugin_name = self._plugins[package_key].ubwidget_class.ub_name if hasattr \
                        (self._plugins[package_key].ubwidget_class, "ub_name") else self._plugins[package_key].plugin_dir
                    if self._plugins[package_key].is_enabled:
                        if self._plugins[package_key].init_on_startup:
                            try:
                                widget = self._plugins[package_key].ubwidget_class()
                            except Exception as exc:
                                widget = FailWidget()
                                widget.set_error_msg(lc.ERROR_WIDGET_INIT.format(wgt_class=self._plugins[package_key].ubwidget_class, traceback_info=traceback.format_exc()))
                            finally:
                                widget.load_key = package_key
                                self._twidget.addTab(widget, self._plugins[package_key].plugin_name)

                        else:
                            dummy_widget = QWidget()
                            dummy_widget.load_key = package_key
                            self._twidget.addTab(dummy_widget, "*" + self._plugins[package_key].plugin_name)

                sys.path.remove(i.dir_abspath)

        self._controlarea.setWidget(self._render_plugins_control_widget())
        utils.ubwidgets_list.clear()
        self._twidget.currentChanged.connect(self._on_tab_changed)
        self._on_tab_changed(0)

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
        for i, key in enumerate(self._plugins.keys()):
            row_counter = i
            label = QLabel()
            if len(plugins[key].plugin_name) > 20:
                name = self._crop_string(plugins[key].plugin_name, 20)
                label.setText(name)
                label.setToolTip(plugins[key].plugin_name)
            else:
                label.setText(plugins[key].plugin_name)
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
        with shelve.open(PLUGINS_DATA_PATH) as data:
            key = plugin.plugin_db_key
            if hasattr(plugin.ubwidget_class, "ub_settings"):
                logging.debug(f"Saving settings for plugin: {plugin.plugin_name}")
                temp = data[key]
                temp.settings_prop_values = plugin.ubwidget_class.ub_settings.propvalues_to_dict()
                data[key] = temp

    @Slot()
    def _on_extra_btn(self):
        plugin = self.sender().plugin
        menu = QMenu(self._parent)
        menu.setFont(QApplication.font())

        def change_init_on_startup():
            nonlocal plugin
            plugin.init_on_startup = not plugin.init_on_startup

        def show_description():
            nonlocal plugin
            dialog = DialogShowDescription(self._parent)
            dialog.setWindowTitle(lc.DESCRIPTION)
            dialog.set_text(plugin.ubwidget_class.ub_description)
            dialog.exec()


        show_description_action = menu.addAction(lc.DESCRIPTION)
        if hasattr(plugin.ubwidget_class, "ub_description") and plugin.ubwidget_class.ub_description:
            show_description_action.triggered.connect(show_description)
        else:
            show_description_action.setEnabled(False)


        open_manual_action = menu.addAction(lc.OPEN_MANUAL)
        open_manual_action.setEnabled(False)

        init_in_startup_action = menu.addAction(lc.INIT_ON_STARTUP)
        init_in_startup_action.setCheckable(True)
        init_in_startup_action.setChecked(plugin.init_on_startup)
        init_in_startup_action.triggered.connect(change_init_on_startup)

        menu.popup(QCursor.pos())

    @Slot()
    def _on_edit_prop_btn(self):
        plugin:PluginListItem = self.sender().plugin
        dialog = DialogEditProperties(self._parent, plugin)
        res = dialog.exec_()
        if res == QDialog.Accepted and not dialog.is_error_occured():
            if (plugin.ubwidget_class.ub_settings.update_data()):
                self._save_plugin_settings(plugin)
                for j in range(self._twidget.count()):
                    if type(self._twidget.widget(j)) is plugin.ubwidget_class:
                        self._twidget.widget(j).settings_changed()
                        break

    @Slot(bool)
    def _on_activate_btn(self, state: bool):
        plugin: PluginListItem = self.sender().plugin
        plugin.is_enabled = state

    def update_plugins(self, update_tabs=False):
        """What does it do?"""
        with shelve.open(PLUGINS_DATA_PATH) as data:
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
                        pl_name = plugin.plugin_name
                        widget = plugin.ubwidget_class()
                        widget.load_key = key
                        self._twidget.addTab(widget, pl_name)
                    else:
                        for j in range(self._twidget.count()):
                            widget = self._twidget.widget(j)
                            if widget.load_key == key:
                                self._twidget.removeTab(j)
                                break


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
                self._twidget.insertTab(index, new_widget, self._plugins[key].plugin_name)
                self._twidget.setCurrentIndex(index)
            self._twidget.currentChanged.connect(self._on_tab_changed)


    def set_qtabwidget(self, twidget:QTabWidget):
        self._twidget = twidget
        twidget.currentChanged.connect(self._on_tab_changed)

    def set_controlarea(self, scroll_area:QScrollArea):
        self._controlarea = scroll_area

    def set_log_view(self, list_view:QListView):
        self._log_model = QStandardItemModel()
        self._log_listview = list_view
        self._log_listview.setModel(self._log_model)


    def _add_log_message(self, msg:str, color:str = "none")->None:
        strtime = time.strftime("%H:%M:%S", time.localtime())
        item = QStandardItem(f"{strtime}\t{msg}")
        match color:
            case "red": item.setBackground(QColor(255, 140, 140))
            case "yellow": item.setBackground(QColor(250, 237, 105))
            case "green": item.setBackground(QColor(142, 255, 140))
        item.setFont(QApplication.font())
        self._log_model.insertRow(0, item)

    def _crop_string(self, s:str, length:int):
        if len(s) <= length:
            return s
        else:
            return(s[0:length-1] + u"…")



