
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal

class CheckableButton(QPushButton):

    state_changed = Signal(bool)

    def __init__(self, state:bool = True, enabled_text: str = "enabled", disabled_text: str = "disabled"):
        super(CheckableButton, self).__init__()
        self.clicked.connect(self._on_clicked)
        self._enabled_text = enabled_text
        self._disabled_text = disabled_text
        self._state = state
        self._update_view()

    def set_enabled_text(self, s:str):
        self._enabled_text = s

    def enabled_text(self):
        return self._enabled_text

    def set_disabled_text(self, s: str):
        self._disabled_text = s

    def disabled_text(self):
        return self._disabled_text

    def set_state(self, state:bool):
        if state is not self._state:
            self._state = state
            self._update_view()
            self.state_changed.emit(state)

    def state(self):
        return self._state

    def _on_clicked(self):
        self.set_state(not self._state)

    def _update_view(self):
        state = self._state
        enabled_style = r"background-color: rgb(72, 255, 72); color: rgb(0, 0, 0)"
        disabled_style = r"background-color: rgb(255, 62, 62); color: rgb(0, 0, 0)"
        self.setText(self._enabled_text if state else self._disabled_text)
        self.setStyleSheet(enabled_style if state else disabled_style)
