
from .Types import UBWidget
import inspect, shelve
from typing import Any


ubwidgets_list = []

def register_ubwidget(widget: UBWidget) -> None:
    global ubwidgets_list
    if (widget not in ubwidgets_list) and (issubclass(widget, UBWidget)):
        ubwidgets_list.append(widget)
    else:
        raise TypeError("Class has to inherit UBWIdget or the class is already registered")


def open_database(ubw_class: UBWidget, flag = "c",  protocol=None, writeback=False) -> Any:
    shelve.open()


