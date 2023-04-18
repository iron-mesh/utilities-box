
from . import Property
from PySide2.QtWidgets import QComboBox, QSizePolicy
from PySide2.QtCore import QCoreApplication


class ComboBoxProperty(Property):

    def __init__(self,  items: list[str], translatable: bool = False, default_value: int=0, name="Unnamed", tool_tip=""):
        self._parameters = {}
        self._parameters["items"] = items
        self._parameters["translatable"] = translatable
        self._parameters["name"] = name
        self._parameters["tool_tip"] = tool_tip

        self._value = default_value

    def get_currentitem_text(self):
        if self._value < len(self._parameters["items"]):
            return self._parameters["items"][self._value]
        else:
            return None

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

    def retranslate(self) -> None:
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self._parameters["tool_tip"]))
        self._widget_ref.clear()
        for el in self._parameters["items"]:
            if self._parameters["translatable"]:
                self._widget_ref.addItem(QCoreApplication.translate("properties", el))
            else:
                self._widget_ref.addItem(el)
        if self._value < len(self._parameters["items"]):
            self._widget_ref.setCurrentIndex(self._value)
        else:
            self._widget_ref.setCurrentIndex(0)
