import sys, os

from PySide6.QtWidgets import QApplication


script_dir:str = os.path.abspath(os.path.dirname(__file__))
index = script_dir.rfind(os.sep)
code_path = script_dir[0:index]
sys.path.append(code_path)

from PyUB.App import UBoxMainWindow
from PyUB import utils
utils.set_home_dir(script_dir)

app = QApplication(sys.argv)
window = UBoxMainWindow()
window.showMaximized()
window.show()
sys.exit(app.exec())

