
from Code.PyUB.Types.Properties import *
from Code.PyUB.Types import PropertyContainer

class UBoxSettings(PropertyContainer):
    style: ComboBoxProperty(items=["MacOS", "Fusion", "Windows", "WindowsVista"], default_value=0, name="Theme")
    font_size: IntProperty(name="Font Size", default_value=10, minimum=8, maximum=48)
    font_family:FontSelectProperty(name="Font")
