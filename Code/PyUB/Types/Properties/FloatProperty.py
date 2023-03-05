
from . import AbstractProperty
from PySide2.QtWidgets import QDoubleSpinBox, QSizePolicy
from PySide2.QtCore import QCoreApplication
import math

class FloatProperty(AbstractProperty):

    def __init__(self, default_value:float = 0.0, name ="Unnamed", minimum = 1.0, maximum = 10.0, single_step = 1.0, decimals = 2, tool_tip = ""):
        self._value = default_value
        self._name = name
        self._minimum = minimum
        self._maximum = maximum
        self._single_step = single_step
        self._decimals = decimals
        self._tool_tip = tool_tip

    def value(self) ->float:
        return self._value

    def set_value(self, value:float) ->None:
        self._value = value

    def get_input_widget(self) -> QDoubleSpinBox:
        self._widget_ref = QDoubleSpinBox()
        self._widget_ref.setValue(self._value)
        self._widget_ref.setMinimum(self._minimum)
        self._widget_ref.setMaximum(self._maximum)
        self._widget_ref.setSingleStep(self._single_step)
        self._widget_ref.setDecimals(self._decimals)
        self.retranslate()

        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        self._widget_ref.setSizePolicy(sizePolicy)

        return self._widget_ref

    def extract_widget_data(self) -> bool:
        has_value_changed:bool = False
        if (hasattr(self, "_widget_ref")) and (not math.isclose(self._value, self._widget_ref.value())):
            self._value = self._widget_ref.value()
            has_value_changed = True
        return has_value_changed

    def get_name(self) -> str:
        return QCoreApplication.translate("properties", self._name)

    def retranslate(self) -> None:
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self._tool_tip))
