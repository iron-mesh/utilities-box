
from . import PropertyValidated
from PySide6.QtWidgets import QComboBox, QSizePolicy
from PySide6.QtCore import QCoreApplication


class ComboBoxProperty(PropertyValidated):
    def __init__(self,  items:list[str], translatable:bool=False, default_value:int=0, name="Unnamed", tool_tip=""):
        self._set_validation(False)
        self.p_items = items
        self.p_translatable = translatable
        self.p_name = name
        self.p_tool_tip = tool_tip
        self._set_validation(True)
        self._value = default_value

    def get_current_item_text(self) -> str:
        return QCoreApplication.translate("properties", self.p_items[self._value]) if self.p_translatable else self.p_items[self._value]

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
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self.p_tool_tip))
        self._widget_ref.clear()
        for el in self.p_items:
            if self.p_translatable:
                self._widget_ref.addItem(QCoreApplication.translate("properties", el))
            else:
                self._widget_ref.addItem(el)
        if self._value < len(self.p_items):
            self._widget_ref.setCurrentIndex(self._value)
        else:
            self._widget_ref.setCurrentIndex(0)

    def validate_value(self, changed_attr:str= ""):
        check_list = ["_value", "p_items"]
        if (changed_attr in check_list) or not changed_attr:
            value = self._value
            if value < 0 or len(self.p_items) == 0:
                self.__dict__["_value"] = 0
            elif value >= len(self.p_items):
                self.__dict__["_value"] = len(self.p_items) - 1
