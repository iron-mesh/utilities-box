import dataclasses, enum
from PySide2.QtCore import QTranslator


@dataclasses.dataclass
class PluginParameters:
    current_lang: str = ""
    is_enabled: bool = True
    settings_prop_values: dict = dataclasses.field(default_factory=dict)
    parameters_dict: dict = dataclasses.field(default_factory=dict)

@dataclasses.dataclass
class AppSettings:
    app_lang: str = ""
    settings_dict: dict = dataclasses.field(default_factory=dict)

class AppDataKeys:
    Language = "lang"
    SettingsDict = "settings"
    CurrentTab = "current_tab"

@dataclasses.dataclass
class PluginListItem:
    module = None
    plugin_name: str = ""
    ubwidget_class = None
    is_enabled: bool = True
    plugin_dir: str = ""
    plugin_translators: list[QTranslator] = dataclasses.field(default_factory=list)
