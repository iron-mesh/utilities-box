
from .import PropertyValidated
from PySide6.QtWidgets import QSpinBox, QSizePolicy
from PySide6.QtCore import QCoreApplication

class IntProperty(PropertyValidated):

    def __init__(self, default_value:int = 0, name="Unnamed", minimum=1, maximum=10, single_step=1, tool_tip=""):
        self._set_validation(False)
        self.p_name = name
        self.p_minimum = minimum
        self.p_maximum = maximum
        self.p_single_step = single_step
        self.p_tool_tip = tool_tip
        self._set_validation(True)
        self._value = default_value

    def get_input_widget(self) -> QSpinBox:
        self._widget_ref = QSpinBox()
        self._widget_ref.setMinimum(self.p_minimum)
        self._widget_ref.setMaximum(self.p_maximum)
        self._widget_ref.setSingleStep(self.p_single_step)
        self._widget_ref.setValue(self._value)
        self.retranslate()

        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        self._widget_ref.setSizePolicy(sizePolicy)

        return self._widget_ref

    def extract_widget_data(self) -> bool:
        has_value_changed: bool = False
        if (hasattr(self, "_widget_ref")) and (self._value != self._widget_ref.value()):
            self._value = self._widget_ref.value()
            has_value_changed = True
        return has_value_changed

    def retranslate(self) -> None:
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self.p_tool_tip))

    def validate_value(self, changed_attr:str=""):
        check_list = ["_value", "p_maximum", "p_minimum"]
        if (changed_attr in check_list) or not changed_attr:
            value = self._value
            if value < self.p_minimum:
                self.__dict__["_value"] = self.p_minimum
            elif value > self.p_maximum:
                self.__dict__["_value"] = self.p_maximum