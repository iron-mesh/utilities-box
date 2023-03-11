import sys, os

def setup():
    proj_name = r"Utilities Box"
    code_path = os.path.abspath("")
    code_path = code_path[0:code_path.find(proj_name)]+proj_name
    sys.path.append(code_path)
    print(code_path)

setup()

from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QFont
from Code.PyUB.App import UtilitiesBoxMainWindow


app = QApplication(sys.argv)
# app.setFont(QFont("ArialBlack", 12, QFont.Normal))
app.setStyle("Fusion")
window = UtilitiesBoxMainWindow()
# window.showMaximized()
window.show()
sys.exit(app.exec_())

