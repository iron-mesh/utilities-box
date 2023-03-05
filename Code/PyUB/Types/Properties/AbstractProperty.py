from abc import ABCMeta, abstractmethod
from typing import Any
from PySide2.QtWidgets import QWidget

class AbstractProperty(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, default_value:Any, name:str = "Unnamed", tool_tip:str ="")->None:
        pass

    @abstractmethod
    def value(self) -> Any:
        pass

    @abstractmethod
    def set_value(self, value: Any) -> None:
        pass

    @abstractmethod
    def get_input_widget(self) -> QWidget:
        pass

    @abstractmethod
    def extract_widget_data(self) -> bool:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def retranslate(self) -> None:
        pass
