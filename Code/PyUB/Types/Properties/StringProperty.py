
from . import AbstractProperty
from PySide2.QtWidgets import QLineEdit
from PySide2.QtCore import QCoreApplication


class StringProperty(AbstractProperty):

    def __init__(self, default_value:str = "", name ="Unnamed", maxlen = 0, input_mask = "", placeholder ="", tool_tip =""):
        self._value = default_value
        self._name = name
        self._placeholder = placeholder
        self._tool_tip = tool_tip
        self._maxlen = maxlen
        self._input_mask = input_mask

    def value(self) -> str:
        return self._value

    def set_value(self, value:str) -> None:
        self._value = value

    def get_input_widget(self) -> QLineEdit:
        self._widget_ref = QLineEdit()
        self.retranslate()
        if self._maxlen > 0:
            self._widget_ref.setMaxLength(self._maxlen)
        if self._input_mask:
            self._widget_ref.setInputMask(self._input_mask)
        self._widget_ref.setText(self._value)
        return self._widget_ref

    def extract_widget_data(self) -> None:
        has_value_changed: bool = False
        if (hasattr(self, "_widget_ref")) and (self._value != self._widget_ref.text()):
            self._value = self._widget_ref.text()
            has_value_changed = True
        return has_value_changed

    def get_name(self) -> str:
        return QCoreApplication.translate("properties", self._name)

    def retranslate(self) -> None:
        self._widget_ref.setPlaceholderText(QCoreApplication.translate("properties", self._placeholder))
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self._tool_tip))
