import sys, os

from PySide6.QtWidgets import QApplication


home_dir:str = os.path.abspath(os.path.dirname(__file__))
index = home_dir.rfind(os.sep)
code_dir = home_dir[0:index]
sys.path.append(code_dir)

from PyUB.App.UBoxMainWindow import UBoxMainWindow
from PyUB import utils

utils.set_home_dir(home_dir)

app = QApplication(sys.argv)
window = UBoxMainWindow()
window.showMaximized()
window.show()
sys.exit(app.exec())

