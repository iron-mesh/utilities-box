
from PyUB.Types import UBWidget
from PySide6.QtWidgets import QPushButton
from .ui_form import Ui_Form
from .Settings import Settings

class CodeLock(UBWidget):

    ub_settings = Settings

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self._init_gui()

        self._code = self.ub_settings.get_property_value("code")

    def _init_gui(self):
        for name in dir(self.ui):
            attr = getattr(self.ui, name)
            if type(attr) is QPushButton:
                attr.clicked.connect(self.on_btn)
        self.ui.lineEdit.setStyleSheet("")
        self.ui.lineEdit.textChanged.connect(self.text_changed)
        self.ui.lineEdit.setInputMask(self.ub_settings.get_property("code").p_input_mask)

    def on_btn(self):
        if not self.ui.lineEdit.isEnabled(): return
        s = self.sender()
        self.ui.lineEdit.setText(self.ui.lineEdit.text() + s.text())

    def text_changed(self, text):
        if len(text) == len(self._code):
            if text == self._code:
                self.ui.lineEdit.setStyleSheet(u"background-color: rgb(85, 255, 127);")
            else:
                self.ui.lineEdit.setStyleSheet(u"background-color: rgb(240, 54, 8);")

            self.ui.lineEdit.setEnabled(False)
            self.id = self.startTimer(5000)

    def timerEvent(self, event) -> None:
        self.ui.lineEdit.setStyleSheet("")
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setEnabled(1)

        self.killTimer(self.id)

    def settings_edit_finished(self, changed:bool) -> None:
        if not changed: return
        self._code = self.ub_settings.get_property_value("code")
        self.ui.lineEdit.clear()