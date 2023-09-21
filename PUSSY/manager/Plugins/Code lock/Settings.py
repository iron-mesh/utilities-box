
from PyUB.Types import PropertyContainer
from PyUB.Types.Properties import StringProperty


class Settings(PropertyContainer):
    code: StringProperty(default_value="12345", input_mask="00000000", name="Код")

