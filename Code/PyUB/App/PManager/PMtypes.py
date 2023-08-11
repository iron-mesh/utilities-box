import dataclasses
from PySide6.QtCore import QTranslator

@dataclasses.dataclass
class PluginListItem:
    """Save plugin's parameters in runtime"""
    module = None
    plugin_name: str = ""
    ubwidget_class = None
    is_enabled: bool = True
    plugin_dir: str = ""
    plugin_translators: list[QTranslator] = dataclasses.field(default_factory=list)

@dataclasses.dataclass
class PluginParameters:
    """Save plugin's parameters on disk"""
    current_lang: str = ""
    is_enabled: bool = True
    settings_prop_values: dict = dataclasses.field(default_factory=dict)
    settings_params_dict: dict = dataclasses.field(default_factory=dict)
