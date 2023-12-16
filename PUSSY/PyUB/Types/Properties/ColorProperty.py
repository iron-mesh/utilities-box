
from . import Property
from PySide6.QtWidgets import QPushButton, QSizePolicy, QColorDialog
from PySide6.QtCore import QCoreApplication, Slot
from PySide6.QtGui import QColor


class ColorProperty(Property):
    def __init__(self, default_value:str="#04104a", name="Unnamed", dialog_title:str="Select Color", tool_tip=""):
        self.p_dialog_title = dialog_title
        self.p_name = name
        self.p_tool_tip = tool_tip
        self._value = default_value

    def get_color(self) -> QColor:
        return QColor(self._value)

    def get_input_widget(self) -> QPushButton:
        self._widget_ref = QPushButton()
        self._widget_ref._color_code = self._value
        self._widget_ref.clicked.connect(self._on_select_color)
        self._widget_ref.setMinimumWidth(100)
        self._update_button_color()
        self.retranslate()
        self._widget_ref.setSizePolicy(QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum))
        return self._widget_ref

    def extract_widget_data(self) -> bool:
        has_value_changed: bool = False
        if hasattr(self, "_widget_ref"):
            widget_value:str = self._widget_ref._color_code
            if self._value != widget_value:
                self._value = widget_value
                has_value_changed = True
        return has_value_changed

    def retranslate(self) -> None:
        self._widget_ref.setToolTip(QCoreApplication.translate("properties", self.p_tool_tip))

    @Slot()
    def _on_select_color(self):
        title = QCoreApplication.translate("properties", self.p_dialog_title)
        current_color = QColor(self._widget_ref._color_code)
        dialog_options = QColorDialog.ColorDialogOption.ShowAlphaChannel

        new_color = QColorDialog.getColor(current_color, title=title, options=dialog_options)
        self._widget_ref._color_code = new_color.name()
        self._update_button_color()

    def _update_button_color(self):
        self._widget_ref.setStyleSheet(f"background-color: {self._widget_ref._color_code};")

