
from ..UBoxSettings import UBoxSettings
from ..FailWidget import FailWidget
from ..ui_forms import Ui_MainWindow
from ..types import PluginListItem, PluginParameters, AppDataKeys
import Code.PyUB.utils as utils
from Code.PyUB.Types.InputWidgets import CheckableButton
from Code.PyUB.Types import UBWidget
import os, sys, shelve, pickle, importlib, traceback, logging
from ..constants import *
from .. import lang_constants as lc
from ..DialogEditProperties import DialogEditProperties
from PySide2.QtWidgets import QMainWindow, QTabWidget, QScrollArea, QProgressDialog,QWidget, QDialog, QSpacerItem, QHBoxLayout, QSizePolicy, QGridLayout, QLabel, QPushButton
from PySide2.QtCore import Qt,Slot


class PluginManager:
    def __init__(self, parent:QMainWindow):
        self._parent = parent

    def load_plugins(self):
        plugins_dir_path = os.path.abspath("Plugins")

        if not hasattr(self, "plugins_loaded"):
            self.plugins_loaded = True
            sys.path.append(plugins_dir_path)
            self._plugins = {}
        self._twidget.clear()

        plugin_dir_list = os.listdir(os.path.abspath(plugins_dir_path))

        with shelve.open(PLUGINS_DATA_PATH) as data:
            for num, dir in enumerate(plugin_dir_list):

                if (dir in FOLDER_NAMES_IGNORE_LIST):
                    continue
                utils.ubwidgets_list.clear()

                if (dir not in self._plugins):
                    self._plugins[dir] = PluginListItem()

                try:
                    if not self._plugins[dir].module:
                        self._plugins[dir].module = importlib.import_module(dir)
                    else:
                        self._plugins[dir].module = importlib.reload(self._plugins[dir].module)
                except Exception:
                    del self._plugins[dir]
                    continue

                if len(utils.ubwidgets_list) == 1 and issubclass(utils.ubwidgets_list[0], UBWidget):
                    self._plugins[dir].plugin_dir = dir
                    self._plugins[dir].ubwidget_class = utils.ubwidgets_list[0]
                else:
                    del self._plugins[dir]
                    continue

                if dir in data:
                    if hasattr(self._plugins[dir].ubwidget_class, "ub_settings"):
                        self._plugins[dir].ubwidget_class.ub_settings.set_properties_from_dict(data[dir].settings_dict)
                    self._plugins[dir].is_enabled = data[dir].is_enabled
                else:
                    pl_params = PluginParameters()
                    if hasattr(self._plugins[dir].ubwidget_class, "ub_settings"):
                        pl_params.settings_dict = self._plugins[dir].ubwidget_class.ub_settings.properties_to_dict()
                    data[dir] = pl_params

                self._plugins[dir].plugin_name = self._plugins[dir].ubwidget_class.ub_name if hasattr \
                    (self._plugins[dir].ubwidget_class, "ub_name") else self._plugins[dir].plugin_dir
                if self._plugins[dir].is_enabled:
                    try:
                        self._twidget.addTab(self._plugins[dir].ubwidget_class(), self._plugins[dir].plugin_name)
                    except Exception as exc:
                        # pass
                        fail_widget = FailWidget()
                        fail_widget.set_error_msg(lc.ERROR_WIDGET_INIT.format(wgt_class=self._plugins[dir].ubwidget_class, traceback_info=traceback.format_exc()))
                        self._twidget.addTab(fail_widget, self._plugins[dir].plugin_name)

        self._controlarea.setWidget(self._render_plugins_control_widget())
        utils.ubwidgets_list.clear()

    def _render_plugins_control_widget(self) -> QWidget:

        def get_edit_properties_handler(plugin: PluginListItem):
            def edit_prop(arg: PluginListItem):
                dialog = DialogEditProperties(self._parent, arg)
                res = dialog.exec_()
                if res == QDialog.Accepted and not dialog.is_error_occured():
                    if (arg.ubwidget_class.ub_settings.update_data()):
                        self._save_plugin_settings(arg)
                        for j in range(self._twidget.count()):
                            if type(self._twidget.widget(j)) is arg.ubwidget_class:
                                self._twidget.widget(j).execute_if_settings_changed()
                                break

            return lambda: edit_prop(plugin)

        def get_switch_handler(arg: PluginListItem):
            def switch_plugin(plugin: PluginListItem, state: bool):
                plugin.is_enabled = state

            return lambda state: switch_plugin(arg, state)

        logging.debug("Creating of plugin page")
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
            layout.addWidget(QLabel(plugins[key].plugin_name), i, 0, Qt.AlignRight)

            switch_btn = CheckableButton(state=plugins[key].is_enabled, enabled_text=lc.SWITCH_PLUGIN_BTN_ENABLED,
                                         disabled_text=lc.SWITCH_PLUGIN_BTN_DISABLED)
            switch_btn.state_changed.connect(get_switch_handler(plugins[key]))
            layout.addWidget(switch_btn, i, 2, Qt.AlignCenter)

            config_btn = QPushButton(lc.CONFIGURATE)
            if hasattr(plugins[key].ubwidget_class, "ub_settings"):
                config_btn.clicked.connect(get_edit_properties_handler(plugins[key]))
                logging.debug(f"Attached property edit handler for class: {plugins[key].ubwidget_class.__name__}")
            else:
                config_btn.setEnabled(False)
            layout.addWidget(config_btn, i, 3, Qt.AlignCenter)

        h_layout.addItem(h_spacer2)
        layout.addItem(v_spacer, row=row_counter + 1, column=3)
        layout.addItem(h_spacer, row=0, column=1)
        return widget

    def _save_plugin_settings(self, plugin: PluginListItem):
        with shelve.open(PLUGINS_DATA_PATH) as data:
            key = plugin.plugin_dir
            if hasattr(plugin.ubwidget_class, "ub_settings"):
                logging.debug(f"Saving settings for class: {plugin.ubwidget_class.__name__}")
                temp = data[key]
                temp.settings_dict = plugin.ubwidget_class.ub_settings.properties_to_dict()
                data[key] = temp

    def update_plugins(self, update_tabs=False):
        with shelve.open(PLUGINS_DATA_PATH) as data:
            for i, plugin in self._plugins.items():
                key = plugin.plugin_dir
                temp_data = data[key]
                logging.debug \
                    (f"{plugin.ubwidget_class.__name__} activity, cur_value: {plugin.is_enabled}, stored value: {temp_data.is_enabled}")
                if temp_data.is_enabled != plugin.is_enabled:
                    temp_data.is_enabled = plugin.is_enabled
                    data[key] = temp_data

                    if (not update_tabs): continue

                    if plugin.is_enabled:
                        pl_name = plugin.ubwidget_class.ub_name if hasattr(plugin.ubwidget_class, "ub_name") else plugin.plugin_dir
                        self._twidget.addTab(plugin.ubwidget_class(), pl_name)
                    else:
                        for j in range(self._twidget.count()):
                            if type(self._twidget.widget(j)) is plugin.ubwidget_class:
                                self._twidget.removeTab(j)
                                break

    @Slot(int)
    def _on_tab_changed(self, index:int):
        pass

    def set_qtabwidget(self, twidget:QTabWidget):
        self._twidget = twidget

    def get_qtabwidget(self) -> QTabWidget:
        return self._twidget

    def set_controlarea(self, scroll_area:QScrollArea):
        self._controlarea = scroll_area

    def get_controlarea(self) -> QScrollArea:
        return self._controlarea