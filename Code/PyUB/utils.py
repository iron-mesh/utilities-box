
from .Types import UBWidget
from .App import parameters
import inspect, shelve, sys
from typing import Any


ubwidgets_list = []

def register_ubwidget(widget: UBWidget) -> None:
    global ubwidgets_list

    if not issubclass(widget, UBWidget):
        raise TypeError(f"Class <{widget.__name__}> must inherit UBWidget class from module <{UBWidget.__module__}>")
    if widget in ubwidgets_list:
        raise Exception(f"Class <{widget.__name__}> is already registered")
    ubwidgets_list.append(widget)

def crop_string(s:str, length:int):
    if len(s) <= length:
        return s
    else:
        return(s[0:length-1] + u"…")

def set_home_dir(path: str) -> None:
    parameters.HOME_DIR = path







