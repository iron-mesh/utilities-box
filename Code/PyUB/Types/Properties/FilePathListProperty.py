from ..InputWidgets import FilePathListInput, PathInputMode
from . import StringListProperty
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QCoreApplication


class FilePathListProperty(StringListProperty):

    def __init__(self, default_value: list[str]=[], name="Unnamed", mode:PathInputMode = PathInputMode.FileOpen, filter="(*.*)", unique_only=False, tool_tip=""):
        super(FilePathListProperty, self).__init__(default_value, name, tool_tip)
        self._parameters["mode"] = mode
        self._parameters["filter"] = filter
        self._parameters["unique_only"] = unique_only

    def get_input_widget(self) -> QWidget:
        self._widget_ref = FilePathListInput()
        self._widget_ref.set_mode(self._parameters["mode"])
        self._widget_ref.set_file_filter(self._parameters["filter"])
        self._widget_ref.set_list(self._value)
        self._widget_ref.unique_only = self._parameters["unique_only"]
        self.retranslate()
        return self._widget_ref


