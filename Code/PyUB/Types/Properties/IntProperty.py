
from .import Property
from PySide2.QtWidgets import QSpinBox, QSizePolicy
from PySide2.QtCore import QCoreApplication

class IntProperty(Property):

    def __init__(self, default_value:int = 0, name="Unnamed", minimum=1, maximum=10, single_step=1, tool_tip=""):
        self._value = default_value
        self._parameters = {}
        self._parameters["name"] = name
        self._parameters["minimum"] = minimum
        self._parameters["maximum"] = maximum
        self._parameters["single_step"] = single_step
        self._parameters["tool_tip"] = tool_tip

    def get_input_widget(self) -> QSpinBox:
        self._widget_ref = QSpinBox()
        self._widget_ref.setValue(self._value)
        self._widget_ref.setMinimum(self._parameters["minimum"])
        self._widget_ref.setMaximum(self._parameters["maximum"])
        self._widget_ref.setSingleStep(self._parameters["single_step"])
        self.retranslate()

        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        self._widget_ref.setSizePolicy(sizePolicy)

        return self._widget_ref

    def extract_widget_data(self) -> None:
        has_value_changed: bool = False
        if (hasattr(self, "_widget_ref")) and (self._value != self._widget_ref.value()):
            self._value = self._widget_ref.value()
            has_value_changed = True
        return has_value_changed

    def retranslate(self) -> None:
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self._parameters["tool_tip"]))

