
from PySide6.QtWidgets import QWidget

class UBWidget(QWidget):

    def __init__(self) -> None:
        super().__init__()

    def retranslate(self) -> None:
        """ The app calls this method when a user changes plugin's language"""
        pass

    def execute_before_closing(self) -> None:
        """ The app calls this method before closing"""
        pass

    def execute_if_settings_changed(self) -> None:
        """ The app calls this method if any property in ub_settings has been changed"""
        pass