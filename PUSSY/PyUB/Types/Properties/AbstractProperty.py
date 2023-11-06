from abc import ABCMeta, abstractmethod
from typing import Any
from PySide6.QtWidgets import QWidget

class AbstractProperty(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, default_value:Any, name:str = "Unnamed") -> None:
        """Init property instance"""
        pass

    @abstractmethod
    def value(self) -> Any:
        """Returns property's value"""
        pass

    @abstractmethod
    def set_value(self, value: Any) -> None:
        """Sets property's value"""
        pass

    @abstractmethod
    def get_parameters_dict(self) -> dict[str, Any]:
        """Returns dictionary of parameters"""
        pass

    @abstractmethod
    def set_parameters_from_dict(self, params: dict[str, Any]) -> None:
        """Sets dictionary of parameters"""
        pass

    @abstractmethod
    def get_input_widget(self) -> QWidget:
        """Returns widget for data input"""
        pass

    @abstractmethod
    def extract_widget_data(self) -> bool:
        """Extracts data from the widget
            Returns True if value has been changed, False - otherwise"""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Returns property's name or its translation"""
        pass

    @abstractmethod
    def retranslate(self) -> None:
        """Sets translations of displayed text"""
        pass
