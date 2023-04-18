
from . import Property
from PySide2.QtWidgets import QCheckBox
from  PySide2.QtCore import Qt
from PySide2.QtCore import QCoreApplication

class BoolProperty(Property):

    def __init__(self, default_value:bool=False, name="Unnamed", tool_tip=""):
        self._value = default_value
        self._parameters = {}
        self._parameters["name"] = name
        self._parameters["tool_tip"] = tool_tip

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

    def retranslate(self) -> None:
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self._parameters["tool_tip"]))