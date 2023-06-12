from ..InputWidgets import FilePathListInput, PathInputMode
from . import StringListProperty
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QCoreApplication


class FilePathListProperty(StringListProperty):

    def __init__(self, default_value: list[str]=[], name="Unnamed", mode:PathInputMode = PathInputMode.FileOpen, filter="(*.*)", unique_only=False, tool_tip=""):
        super(FilePathListProperty, self).__init__(default_value, name, tool_tip)
        self.p_mode = mode
        self.p_filter = filter
        self.p_unique_only = unique_only

    def get_input_widget(self) -> QWidget:
        self._widget_ref = FilePathListInput()
        self._widget_ref.set_mode(self.p_mode)
        self._widget_ref.set_file_filter(self.p_filter)
        self._widget_ref.set_list(self._value)
        self._widget_ref.unique_only = self.p_unique_only
        self.retranslate()
        return self._widget_ref


