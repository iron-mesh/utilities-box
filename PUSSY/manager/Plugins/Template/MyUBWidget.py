
from PyUB.Types import UBWidget, UBHelper
from .MySettings import MySettings


class MyUBWidget(UBWidget):

    ub_settings = MySettings #optional field
    ub_name = "My plugin" #optional field

    def __init__(self):
        super().__init__()
        #Your code...

    def retranslate(self) -> None: #optional method
        pass

    def app_closing(self) -> None: #optional method
        pass

    def deactivated(self) -> None: #optional method
        pass

    def settings_edit_started(self) -> None: #optional method
        pass

    def settings_edit_finished(self, changed:bool) -> None: #optional method
        pass