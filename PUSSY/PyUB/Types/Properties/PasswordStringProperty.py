
from . import StringProperty
from PySide6.QtWidgets import QLineEdit


class PasswordStringProperty(StringProperty):

    def get_input_widget(self) -> QLineEdit:
        self._widget_ref = QLineEdit()
        self.retranslate()
        if self.p_maxlen > 0:
            self._widget_ref.setMaxLength(self.p_maxlen)
        if self.p_input_mask:
            self._widget_ref.setInputMask(self.p_input_mask)
        self._widget_ref.setText(self._value)
        self._widget_ref.setEchoMode(QLineEdit.Password)
        return self._widget_ref


