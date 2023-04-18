
from . import Property
from PySide2.QtWidgets import QLineEdit
from PySide2.QtCore import QCoreApplication
from ..InputWidgets import PathInput, PathInputMode


class FilePathProperty(Property):

    def __init__(self, default_value:str = "", name="Unnamed", mode:PathInputMode=PathInputMode.FileOpen, dialog_title="Open file/folder", filter="(*.*)", placeholder="", tool_tip=""):
        self._value = default_value
        self._parameters = {}
        self._parameters["name"] = name
        self._parameters["mode"] = mode
        self._parameters["dialog_title"] = dialog_title
        self._parameters["filter"] = filter
        self._parameters["placeholder"] = placeholder
        self._parameters["tool_tip"] = tool_tip

    def get_input_widget(self) -> PathInput:
        self._widget_ref = PathInput()
        self._widget_ref.set_mode(self._parameters["mode"])
        self._widget_ref.set_path(self._value)
        self.retranslate()
        return self._widget_ref

    def extract_widget_data(self) -> None:
        has_value_changed: bool = False
        if (hasattr(self, "_widget_ref")) and (self._value != self._widget_ref.get_path()):
            self._value = self._widget_ref.get_path()
            has_value_changed = True
        return has_value_changed

    def retranslate(self) -> None:
        self._widget_ref.set_placeholder(QCoreApplication.translate("properties", self._parameters["placeholder"]))
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self._parameters["tool_tip"]))
        self._widget_ref.set_window_title(QCoreApplication.translate("properties", self._parameters["dialog_title"]))
        self._widget_ref.set_file_filter(QCoreApplication.translate("properties", self._parameters["filter"]))
