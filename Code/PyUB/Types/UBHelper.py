
from . import UBWidget
class UBHelper:

    def __init__(self, key:UBWidget):
        if issubclass(key, UBWidget):
            self._key = key
        else:
            raise TypeError("Parameter <key> is not subclass of UBWidget ")

    def save_settings_parameters(self):
        '''Save settings parameters attached to <ub_settings> on HDD'''

