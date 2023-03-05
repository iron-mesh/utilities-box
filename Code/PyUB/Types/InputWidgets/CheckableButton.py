
from PySide2.QtWidgets import QPushButton
from PySide2.QtCore import Signal

class CheckableButton(QPushButton):

    state_changed = Signal(bool)

    def __init__(self, state:bool = True, enabled_text: str = "enabled", disabled_text: str = "disabled"):
        super(CheckableButton, self).__init__()
        self.clicked.connect(self._on_clicked)
        self._enabled_text = enabled_text
        self._disabled_text = disabled_text
        self.set_state(state)

    def set_enabled_text(self, s:str):
        self._enabled_text = s

    def enabled_text(self):
        return self._enabled_text

    def set_disabled_text(self, s: str):
        self._disabled_text = s

    def disabled_text(self):
        return self._disabled_text

    def set_state(self, state:bool):
        self._state = state
        enabled_style = r"background-color: rgb(72, 255, 72);"
        disabled_style = r"background-color: rgb(255, 62, 62)"
        self.setText(self._enabled_text if state else self._disabled_text)
        self.setStyleSheet(enabled_style if state else disabled_style)
        self.state_changed.emit(state)

    def state(self):
        return self._state

    def _on_clicked(self):
        self.set_state(not self._state)