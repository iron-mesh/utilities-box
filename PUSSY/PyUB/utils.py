
from .Types import UBWidget

__all__ = ['register_ubwidget']
_ubwidgets_list = []

def register_ubwidget(widget: UBWidget) -> None:
    global _ubwidgets_list

    if not issubclass(widget, UBWidget):
        raise TypeError(f"Class <{widget.__name__}> must inherit UBWidget class from module <{UBWidget.__module__}>")
    if widget in _ubwidgets_list:
        raise Exception(f"Class <{widget.__name__}> is already registered")
    _ubwidgets_list.append(widget)







