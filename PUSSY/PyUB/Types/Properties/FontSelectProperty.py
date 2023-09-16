
from . import Property
from PySide6.QtWidgets import QSizePolicy, QFontComboBox
from PySide6.QtGui import QFont
from PySide6.QtCore import QCoreApplication


class FontSelectProperty(Property):

    def __init__(self, default_value:int=0, name="Unnamed", tool_tip=""):
        self._value = default_value
        self.p_name = name
        self.p_tool_tip = tool_tip

    def get_input_widget(self) -> QFontComboBox:
        self._widget_ref = QFontComboBox()
        self.retranslate()
        self._widget_ref.setSizePolicy(QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed))
        self._widget_ref.setCurrentIndex(self._value)
        return self._widget_ref

    def get_current_font(self) -> QFont:
        if (hasattr(self, "_widget_ref")):
            return self._widget_ref.currentFont()
        else:
            font_combobox = QFontComboBox()
            font_combobox.setCurrentIndex(self._value)
            return font_combobox.currentFont()

    def extract_widget_data(self) -> bool:
        has_value_changed: bool = False
        if (hasattr(self, "_widget_ref")) and (self._value != self._widget_ref.currentIndex()):
            self._value = self._widget_ref.currentIndex()
            has_value_changed = True
        return has_value_changed

    def retranslate(self) -> None:
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self.p_tool_tip))