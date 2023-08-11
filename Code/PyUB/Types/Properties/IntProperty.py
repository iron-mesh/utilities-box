
from .import Property
from PySide6.QtWidgets import QSpinBox, QSizePolicy
from PySide6.QtCore import QCoreApplication

class IntProperty(Property):

    def __init__(self, default_value:int = 0, name="Unnamed", minimum=1, maximum=10, single_step=1, tool_tip=""):
        self._value = default_value
        self.p_name = name
        self.p_minimum = minimum
        self.p_maximum = maximum
        self.p_single_step = single_step
        self.p_tool_tip = tool_tip

    def get_input_widget(self) -> QSpinBox:
        self._widget_ref = QSpinBox()
        self._widget_ref.setValue(self._value)
        self._widget_ref.setMinimum(self.p_minimum)
        self._widget_ref.setMaximum(self.p_maximum)
        self._widget_ref.setSingleStep(self.p_single_step)
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

    def set_value(self, value: int) -> None:
        if value < self.p_minimum:
            self._value = self.p_minimum
        elif value > self.p_maximum:
            self._value = self.p_maximum
        else:
            self._value = value

    def retranslate(self) -> None:
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self.p_tool_tip))

