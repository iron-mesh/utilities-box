import logging

from .import PropertyValidated
from PySide6.QtWidgets import QSizePolicy, QCheckBox, QGroupBox, QGridLayout
from PySide6.QtCore import QCoreApplication, Qt

class BoolListProperty(PropertyValidated):

    def __init__(self, items:list[str]=[], default_value:list[bool]=[], translatable:bool=False, name="Unnamed", tool_tip="", columns:int=1):
        self._set_validation(False)
        self.p_items = items
        self.p_name = name
        self.p_translatable = translatable
        self.p_tool_tip = tool_tip
        self.p_columns = columns
        self._set_validation(True)
        self._value = default_value

    def get_input_widget(self) -> QGroupBox:
        col_count = 1 if self.p_columns < 1 else self.p_columns
        self._widget_ref = QGroupBox()
        self._widget_ref.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred))
        layout = QGridLayout(self._widget_ref)

        self._checkbox_list = []
        for index, item in enumerate(self._value):
            col = index % col_count
            row = index // col_count
            checkbox = QCheckBox()
            checkbox.setCheckState(Qt.CheckState.Checked if item else Qt.CheckState.Unchecked)
            layout.addWidget(checkbox, row, col)
            self._checkbox_list.append(checkbox)

        self.retranslate()
        return self._widget_ref

    def extract_widget_data(self) -> bool:
        has_value_changed: bool = False
        widget_values = [(True if i.checkState() == Qt.CheckState.Checked else False) for i in self._checkbox_list]
        logging.debug(widget_values)
        if (hasattr(self, "_widget_ref")) and (self._value != widget_values):
            self._value = widget_values
            has_value_changed = True
        return has_value_changed

    def retranslate(self) -> None:
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self.p_tool_tip))

        for i, checkbox in enumerate(self._checkbox_list):
            text = QCoreApplication.translate("properties", self.p_items[i]) if self.p_translatable else self.p_items[i]
            checkbox.setText(text)

    def validate_value(self, changed_attr:str=""):
        check_list = ["_value", "p_items"]
        if (changed_attr in check_list) or not changed_attr:
            if len(self._value) < len(self.p_items):
                dif = len(self.p_items) - len(self._value)
                self._value.extend([False for i in range(dif)])
            elif len(self._value) > len(self.p_items):
                self.__dict__["_value"] = self._value[0:len(self.p_items)]