

from PySide6.QtCore import QMutex, QMutexLocker, QReadWriteLock, QThread
import sys


class resource:
    value:str = ""
    locker = QReadWriteLock

    @classmethod
    def change(cls, s):
        cls.locker.lockForRead()
        cls.value = s
        cls.locker.unlock()



class thread(QThread):
    resource: int = 0

    def run(self) -> None:
        for i in range(100):
            resource.change(f"Value {i}")
            print(resource.value)



def click():
    thread = QThread
    thread.start(QThread.NormalPriority)


app = QApplication(sys.argv)
# app.setFont(QFont("ArialBlack", 12, QFont.Normal))
app.setStyle("Fusion")
btn = Q
window = QWidget()
# window.showMaximized()
window.show()
sys.exit(app.exec_())