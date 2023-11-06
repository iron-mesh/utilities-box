
from . import PropertyValidated
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QRegularExpressionValidator


class StringProperty(PropertyValidated):

    def __init__(self, default_value:str="", name="Unnamed", maxlen=0, input_mask="", placeholder="", tool_tip="", re_validator=""):
        self._switch_validation(False)
        self.p_name = name
        self.p_placeholder = placeholder
        self.p_tool_tip = tool_tip
        self.p_maxlen = maxlen
        self.p_input_mask = input_mask
        self.p_re_validator = re_validator
        self._switch_validation(True)
        self._value = default_value

    def get_input_widget(self) -> QLineEdit:
        self._widget_ref = self._gen_widget()
        self.retranslate()
        return self._widget_ref

    def extract_widget_data(self) -> None:
        has_value_changed: bool = False
        if (hasattr(self, "_widget_ref")) and (self._value != self._widget_ref.text()):
            self._value = self._widget_ref.text()
            has_value_changed = True
        return has_value_changed

    def validate_value(self, changed_attr: str = "") -> None:
        check_list = ["_value", "p_maxlen", "p_input_mask", "p_re_validator"]
        if (changed_attr in check_list) or not changed_attr:
            dummy_widget = self._gen_widget()
            if dummy_widget.hasAcceptableInput():
                self.__dict__["_value"] = dummy_widget.text()
            else:
                self.__dict__["_value"] = ""

    def _gen_widget(self) -> QLineEdit:
        widget = QLineEdit()
        if self.p_maxlen > 0:
            widget.setMaxLength(self.p_maxlen)
        widget.setInputMask(self.p_input_mask)
        if self.p_re_validator:
            validator = QRegularExpressionValidator(self.p_re_validator)
            widget.setValidator(validator)
        widget.setText(self._value)

        return widget

    def retranslate(self) -> None:
        self._widget_ref.setPlaceholderText(QCoreApplication.translate("properties", self.p_placeholder))
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self.p_tool_tip))
