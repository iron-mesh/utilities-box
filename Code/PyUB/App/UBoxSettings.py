
from Code.PyUB.Types.Properties import *
from Code.PyUB.Types import PropertyContainer

class UBoxSettings(PropertyContainer):
    style: ComboBoxProperty(items=["Fusion", "Windows"], default_value=0, name="Visual style")
    font_size: IntProperty(name="Font Size", default_value=10, minimum=8, maximum=20)
