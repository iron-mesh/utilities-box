
from PySide6.QtWidgets import QWidget

class UBWidget(QWidget):
    #ub_name = "type plugin name"
    #ub_settings = <link PropertyContainer class>
    #ub_description = "Plugin description"

    def __init__(self) -> None:
        super().__init__()

    def retranslate(self) -> None:
        """ The app calls this method when a user changes plugin's language"""
        pass

    def app_closing(self) -> None:
        """ The app calls this method before closing"""
        pass

    def settings_changed(self) -> None:
        """ The app calls this method if any property in ub_settings has been changed"""
        pass