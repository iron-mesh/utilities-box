from ..InputWidgets import NamedFilePathListInput, PathInputMode
from . import Property
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QCoreApplication


class NamedFilePathListProperty(Property):

    def __init__(self, default_value: list[tuple]=[], name="Unnamed", mode:PathInputMode = PathInputMode.Directory, filter="(*.*)", tool_tip=""):
        super().__init__(default_value, name)
        self.p_mode = mode
        self.p_filter = filter
        self.p_tool_tip = tool_tip

    def get_input_widget(self) -> QWidget:
        self._widget_ref = NamedFilePathListInput()
        self._widget_ref.set_mode(self.p_mode)
        self._widget_ref.set_file_filter(self.p_filter)
        self._widget_ref.set_list(self._value)
        self.retranslate()
        return self._widget_ref

    def extract_widget_data(self) -> bool:
        if hasattr(self, "_widget_ref") and self._widget_ref.get_list() != self._value:
            self._value = self._widget_ref.get_list()
            return True
        else:
            return False

    def retranslate(self) -> None:
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self.p_tool_tip))