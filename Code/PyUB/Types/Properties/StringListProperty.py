
from . import AbstractProperty
from ..InputWidgets import StringListInput
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QCoreApplication


class StringListProperty(AbstractProperty):

    def __init__(self, default_value: list[str]=[""], name="Unnamed", tool_tip=""):
        self._value = default_value
        self._name = name
        self._tool_tip = tool_tip


    def value(self) -> list[str]:
        return self._value

    def set_value(self, value: list[str]) -> None:
        self._value = value

    def get_input_widget(self) -> QWidget:
        self._widget_ref = StringListInput()
        self._widget_ref.set_list(self._value)
        self.retranslate()
        return self._widget_ref

    def extract_widget_data(self) -> bool:
        if self._widget_ref.get_list() != self._value:
            self._value = self._widget_ref.get_list()
            return True
        else:
            return False

    def get_name(self) -> str:
        return QCoreApplication.translate("properties", self._name)

    def retranslate(self) -> None:
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self._tool_tip))

