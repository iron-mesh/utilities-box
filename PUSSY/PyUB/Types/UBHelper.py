
from . import UBWidget
from PySide6.QtCore import QMutex, QMutexLocker
from PyUB.App.PManager.PluginManager import PluginManager
from PyUB.App.PManager.PMtypes import Commands
class UBHelper:
    _mutex = QMutex()
    _plugin_manager:PluginManager = None

    def __init__(self, key_class:UBWidget):

        if issubclass(key_class, UBWidget):
            self._key_class = key_class
        else:
            raise TypeError("Parameter <key> is not subclass of UBWidget ")

    def save_settings_parameters(self):
        '''Save settings parameters attached to <ub_settings>, on HDD'''
        self._plugin_manager.exec_command(self._key_class, Commands.SaveSettingsParameters)

    def open_localstorage(self, flag='c', protocol=None, writeback=False):
        """Open a persistent dictionary-like object"""
        with QMutexLocker(self._mutex):
            return self._plugin_manager.exec_command(self._key_class, Commands.GetLocalStorage, f=flag, p=protocol, w=writeback)

    def get_plugin_dir(self)->str:
        """ Returns absolute path to plugin directory"""
        return self._plugin_manager.exec_command(self._key_class, Commands.GetPluginDir)

    @classmethod
    def set_plugin_manager(cls, plugin_manager:PluginManager):
        cls._plugin_manager = plugin_manager


