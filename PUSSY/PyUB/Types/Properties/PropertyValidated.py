from typing import Any
from . import Property
class PropertyValidated(Property):

    def __init__(self, default_value: Any, name: str = "Unnamed", tool_tip="") -> None:
        self._switch_validation(False)
        super().__init__(default_value, name, tool_tip)
        self._switch_validation(True)
        self.validate_value()

    def __setattr__(self, key, value):
        self.__dict__[key] = value

        if self._do_validation:
            self.validate_value(key)


    def validate_value(self, changed_attr:str=""):
        """Performs validation of property's value
        Receives: changed_attr - name of changed attribute"""
        check_list = ["_value"]
        if (changed_attr in check_list) or not changed_attr:
            pass

    def _switch_validation(self, state:bool=True):
        self.__dict__["_do_validation"] = state

    def set_parameters_from_dict(self, params: dict[str, Any]) -> None:
        """ Set property parameters from dict"""
        for key, val in params.items():
            if hasattr(self, key) and type(getattr(self, key)) is type(val):
                self.__dict__[key] = val

        self.validate_value()