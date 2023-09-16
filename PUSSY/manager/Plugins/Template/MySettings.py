print("load settings")

from PyUB.Types import PropertyContainer
from PyUB.Types.Properties import *

class MySettings(PropertyContainer):
    property1: IntProperty(name="It's integer", default_value=5, single_step=1, minimum=0, maximum=110, tool_tip="input random number")