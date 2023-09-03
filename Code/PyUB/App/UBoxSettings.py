
from ..Types.Properties import *
from ..Types import PropertyContainer
from ..Types.InputWidgets import PathInputMode

class UBoxSettings(PropertyContainer):
    style: ComboBoxProperty(items=["MacOS", "Fusion", "Windows", "WindowsVista"], default_value=0, name="Theme")
    font_size: IntProperty(name="Font Size", default_value=10, minimum=8, maximum=48)
    font_family:FontSelectProperty(name="Font")
    external_plugin_dir:NamedFilePathListProperty(name="External Plugin\nDirectory", mode=PathInputMode.Directory)
