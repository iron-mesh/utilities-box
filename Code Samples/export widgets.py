from PySide6.QtWidgets import QWidget,QPushButton, QVBoxLayout, QApplication, QTabWidget
import sys
import reg_widget



class CustomWidget1(QWidget):

    def __init__(self):
        super().__init__()
        self.lay = QVBoxLayout()
        self.lay.addWidget(QPushButton("Hello world"))
        self.setLayout(self.lay)

class CustomWidget2(QWidget):

    def __init__(self):
        super().__init__()
        self.lay = QVBoxLayout()
        self.lay.addWidget(QPushButton("Hello world 2"))
        self.setLayout(self.lay)


app = QApplication(sys.argv)
app.setStyle("Fusion")

reg_widget.register_widget(CustomWidget1())
reg_widget.register_widget(CustomWidget2())

window = QWidget()
tabs = QTabWidget()

print(reg_widget.widgets)
for i in reg_widget.widgets:
    tabs.addTab(i, "name")

layout = QVBoxLayout()
layout.addWidget(tabs)

window.setLayout(layout)
window.resize(400,300)
window.show()
sys.exit(app.exec_())