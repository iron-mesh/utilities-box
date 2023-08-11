
from typing import Any
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QCoreApplication
from . import AbstractProperty


class Property(AbstractProperty):
    def __init__(self, default_value: Any, name: str = "Unnamed") -> None:
        """Init property instance"""
        self._value = default_value
        self.p_name = name

    def value(self) -> Any:
        """Returns property's value"""
        return self._value

    def set_value(self, value: Any) -> None:
        """Sets property's value"""
        self._value = value

    def get_parameters_dict(self) -> dict[str, Any]:
        """ Get property parameters dict"""
        return {key: value for key, value in vars(self).items() if key[0:2] == "p_"}

    def set_parameters_from_dict(self, params: dict[str, Any]) -> None:
        """ Set property parameters from dict"""
        for key, val in params.items():
            if hasattr(self, key) and type(getattr(self, key)) is type(val):
                setattr(self, key, val)

    def get_input_widget(self) -> QWidget:
        """Returns widget for data input"""
        pass

    def extract_widget_data(self) -> bool:
        """Extracts data from widget
        Returns True if value was changed, False - otherwise"""
        pass

    def get_name(self) -> str:
        """Returns property's name or its translation"""
        return QCoreApplication.translate("properties", self.p_name)

    def retranslate(self) -> None:
        pass
