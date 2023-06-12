
from . import Property
from ..InputWidgets import StringListInput
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QCoreApplication


class StringListProperty(Property):

    def __init__(self, default_value: list[str]=[""], name="Unnamed", tool_tip=""):
        self._value = default_value
        self.p_name = name
        self.p_tool_tip = tool_tip

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

    def retranslate(self) -> None:
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self.p_tool_tip))

