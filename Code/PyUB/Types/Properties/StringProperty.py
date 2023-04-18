
from . import Property
from PySide2.QtWidgets import QLineEdit
from PySide2.QtCore import QCoreApplication


class StringProperty(Property):

    def __init__(self, default_value:str = "", name ="Unnamed", maxlen = 0, input_mask = "", placeholder ="", tool_tip =""):
        self._value = default_value
        self._parameters = {}
        self._parameters["name"] = name
        self._parameters["placeholder"] = placeholder
        self._parameters["tool_tip"] = tool_tip
        self._parameters["maxlen"] = maxlen
        self._parameters["input_mask"] = input_mask

    def get_input_widget(self) -> QLineEdit:
        self._widget_ref = QLineEdit()
        self.retranslate()
        if self._parameters["maxlen"] > 0:
            self._widget_ref.setMaxLength(self._parameters["maxlen"])
        if self._parameters["input_mask"]:
            self._widget_ref.setInputMask(self._parameters["input_mask"])
        self._widget_ref.setText(self._value)
        return self._widget_ref

    def extract_widget_data(self) -> None:
        has_value_changed: bool = False
        if (hasattr(self, "_widget_ref")) and (self._value != self._widget_ref.text()):
            self._value = self._widget_ref.text()
            has_value_changed = True
        return has_value_changed

    def retranslate(self) -> None:
        self._widget_ref.setPlaceholderText(QCoreApplication.translate("properties", self._parameters["placeholder"]))
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self._parameters["tool_tip"]))
