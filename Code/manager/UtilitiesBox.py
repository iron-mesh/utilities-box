import sys, os, traceback

def setup():
    script_dir:str = os.path.abspath(os.path.dirname(__file__))
    os.chdir(script_dir)
    index = script_dir.rfind(os.sep)
    code_path = script_dir[0:index]
    sys.path.append(code_path)
    print(os.path.abspath("Code"))
    print(code_path)

setup()

try:
    from PySide6.QtWidgets import QApplication
    from PyUB.App import UBoxMainWindow
except:
    print(traceback.format_exc())
    input()



app = QApplication(sys.argv)
window = UBoxMainWindow()
window.showMaximized()
window.show()
sys.exit(app.exec())

