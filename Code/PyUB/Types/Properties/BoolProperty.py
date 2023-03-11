
from . import AbstractProperty
from PySide2.QtWidgets import QCheckBox
from  PySide2.QtCore import Qt
from PySide2.QtCore import QCoreApplication

class BoolProperty(AbstractProperty):

    def __init__(self, default_value:bool = False, name = "Unnamed", tool_tip = ""):
        self._value = default_value
        self._name = name
        self._tool_tip = tool_tip

    def value(self) ->bool:
        return self._value

    def set_value(self, value:bool) ->None:
        self._value = value

    def get_input_widget(self) -> QCheckBox:
        self._widget_ref = QCheckBox()
        self._widget_ref.setCheckState(Qt.Checked if self._value else Qt.Unchecked)
        self.retranslate()
        return self._widget_ref

    def extract_widget_data(self) -> bool:
        has_value_changed: bool = False
        if hasattr(self, "_widget_ref"):
            widget_value: bool = True if self._widget_ref.checkState() == Qt.Checked else False
            if self._value != widget_value:
                self._value = widget_value
                has_value_changed = True
        return has_value_changed

    def get_name(self) -> str:
        return QCoreApplication.translate("properties", self._name)

    def retranslate(self) -> None:
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self._tool_tip))