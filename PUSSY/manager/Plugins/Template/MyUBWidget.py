print("my class")


from PyUB.Types import UBWidget, UBHelper
from .MySettings import MySettings


class MyUBWidget(UBWidget):

    ub_settings = MySettings
    ub_name = "Your plugin's name"

    def __init__(self):
        super().__init__()
        #Your code...

    def retranslate(self) -> None: #optional method
        pass

    def app_closing(self) -> None: #optional method
        pass

    def settings_changed(self) -> None: #optional method
        pass