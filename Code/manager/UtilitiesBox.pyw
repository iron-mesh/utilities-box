import sys, os

def setup():
    proj_name = r"Utilities Box"
    code_path = os.path.abspath("")
    code_path = code_path[0:code_path.find(proj_name)]+proj_name
    sys.path.append(code_path)
    print(code_path)

setup()

from PySide6.QtWidgets import QApplication
from Code.PyUB.App import UBoxMainWindow


app = QApplication(sys.argv)
window = UBoxMainWindow()
window.showMaximized()
window.show()
sys.exit(app.exec())

