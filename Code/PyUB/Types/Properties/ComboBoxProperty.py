
from . import AbstractProperty
from PySide2.QtWidgets import QComboBox, QSizePolicy
from PySide2.QtCore import QCoreApplication


class ComboBoxProperty(AbstractProperty):

    def __init__(self,  items: list[str], translatable: bool = False, default_value: int=0, name="Unnamed", tool_tip=""):
        self._items = items
        self._translatable = translatable
        self._value = default_value
        self._name = name
        self._tool_tip = tool_tip

    def value(self) -> str:
        return self._value

    def set_value(self, value: str) -> None:
        self._value = value

    def get_input_widget(self) -> QComboBox:
        self._widget_ref = QComboBox()
        self.retranslate()

        self._widget_ref.setSizePolicy(QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed))
        return self._widget_ref

    def extract_widget_data(self) -> bool:
        has_value_changed: bool = False
        if (hasattr(self, "_widget_ref")) and (self._value != self._widget_ref.currentIndex()):
            self._value = self._widget_ref.currentIndex()
            has_value_changed = True
        return has_value_changed

    def get_name(self) -> str:
        return QCoreApplication.translate("properties", self._name)

    def retranslate(self) -> None:
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self._tool_tip))
        self._widget_ref.clear()
        for el in self._items:
            if self._translatable:
                self._widget_ref.addItem(QCoreApplication.translate("properties", el))
            else:
                self._widget_ref.addItem(el)
        self._widget_ref.setCurrentIndex(self._value)
