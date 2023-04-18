
from . import StringProperty
from PySide2.QtWidgets import QLineEdit


class PasswordStringProperty(StringProperty):

    def get_input_widget(self) -> QLineEdit:
        self._widget_ref = QLineEdit()
        self.retranslate()
        if self._parameters["maxlen"] > 0:
            self._widget_ref.setMaxLength(self._parameters["maxlen"])
        if self._parameters["input_mask"]:
            self._widget_ref.setInputMask(self._parameters["input_mask"])
        self._widget_ref.setText(self._value)
        self._widget_ref.setEchoMode(QLineEdit.Password)
        return self._widget_ref


