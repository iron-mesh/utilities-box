
from Code.PyUB.Types.Properties import *
from Code.PyUB.Types import PropertyContainer

class UBoxSettings(PropertyContainer):
    font_size: IntProperty(name="Font Size", default_value=10, minimum=8, maximum=20)