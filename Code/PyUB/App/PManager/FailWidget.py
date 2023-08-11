
from ..ui_forms.ui_plugin_init_failed import Ui_Form
from PySide6.QtWidgets import QWidget, QPlainTextEdit


class FailWidget(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.plainTextEdit.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.ui.plainTextEdit.setReadOnly(True)

    def set_error_msg(self, text: str) -> None:
        self.ui.plainTextEdit.setPlainText(text)