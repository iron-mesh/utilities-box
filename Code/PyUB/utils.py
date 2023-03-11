
from .Types import UBWidget
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


def open_database(ubw_class: UBWidget, flag="c", protocol=None, writeback=False) -> Any:
    shelve.open()


