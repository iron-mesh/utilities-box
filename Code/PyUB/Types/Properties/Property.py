
from typing import Any
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QCoreApplication
from . import AbstractProperty

class Property(AbstractProperty):
    def __init__(self, default_value: Any, name: str = "Unnamed") -> None:
        """Init property instance"""
        self._value = default_value
        self._parameters = {}
        self._parameters["name"] = name

    def value(self) -> Any:
        """Returns property's value"""
        return self._value

    def set_value(self, value: Any) -> None:
        """Sets property's value"""
        self._value = value

    def get_parameters_dict(self) -> dict[str, Any]:
        """ Get property parameters dict"""
        return self._parameters

    def set_parameters_from_dict(self, params: dict[str, Any]) -> None:
        """ Set property parameters from dict"""
        for key in params.keys():
            if (key in self._parameters) and isinstance(params[key], type(self._parameters[key])):
                self._parameters[key] = params[key]

    def get_input_widget(self) -> QWidget:
        """Returns widget for data input"""
        pass

    def extract_widget_data(self) -> bool:
        """Extracts data from widget
        Returns True if value was changed, False - otherwise"""
        pass

    def get_name(self) -> str:
        """Returns property's name or its translation"""
        return QCoreApplication.translate("properties", self._parameters["name"])

    def retranslate(self) -> None:
        pass
