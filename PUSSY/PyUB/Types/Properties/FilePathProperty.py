
from . import Property
from PySide6.QtCore import QCoreApplication
from ..InputWidgets import PathInputIC, PathInputMode


class FilePathProperty(Property):

    def __init__(self, default_value:str = "", name="Unnamed", mode:PathInputMode=PathInputMode.FileOpen, dialog_title="Open file/folder", filter="(*.*)", placeholder="", tool_tip=""):
        self._value = default_value
        self.p_name = name
        self.p_mode = mode
        self.p_dialog_title = dialog_title
        self.p_filter = filter
        self.p_placeholder = placeholder
        self.p_tool_tip = tool_tip

    def get_input_widget(self) -> PathInputIC:
        self._widget_ref = PathInputIC()
        self._widget_ref.set_mode(self.p_mode)
        self._widget_ref.set_path(self._value)
        self.retranslate()
        return self._widget_ref

    def extract_widget_data(self) -> None:
        has_value_changed: bool = False
        if (hasattr(self, "_widget_ref")) and (self._value != self._widget_ref.path()):
            self._value = self._widget_ref.path()
            has_value_changed = True
        return has_value_changed

    def retranslate(self) -> None:
        self._widget_ref.setPlaceholderText(QCoreApplication.translate("properties", self.p_placeholder))
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self.p_tool_tip))
        self._widget_ref.set_window_title(QCoreApplication.translate("properties", self.p_dialog_title))
        self._widget_ref.set_file_filter(QCoreApplication.translate("properties", self.p_filter))
