import dataclasses, enum
from PySide6.QtCore import QTranslator
from collections import namedtuple

@dataclasses.dataclass
class PluginListItem:
    """Save plugin parameters in runtime"""
    module = None
    is_valid:bool = True
    is_enabled: bool = True
    plugin_name: str = ""
    plugin_short_name: str = ""
    ubwidget_class = None
    init_on_startup: bool = False
    plugin_dir_name: str = ""
    plugin_db_key: str = ""
    plugin_dirsite = ""
    plugin_translators: list[QTranslator] = dataclasses.field(default_factory=list)
    default_settings_values_dict: dict = dataclasses.field(default_factory=dict)
    default_settings_params_dict: dict = dataclasses.field(default_factory=dict)

@dataclasses.dataclass
class PluginParameters:
    """Save plugin parameters on disk"""
    current_lang: str = ""
    enabled: bool = True
    init_on_startup: bool = False
    settings_prop_values: dict = dataclasses.field(default_factory=dict)
    settings_params_dict: dict = dataclasses.field(default_factory=dict)

@dataclasses.dataclass
class PackageDirItem:
    """Describe item of folder with packages"""
    dir_nickname:str = ""
    dir_abspath:str = ""
    package_list:list[str] = dataclasses.field(default_factory=list)


@enum.unique
class Commands(enum.IntEnum):
    GetPluginDir = 0
    GetLocalStorage = 1
    SaveSettingsParameters = 2

