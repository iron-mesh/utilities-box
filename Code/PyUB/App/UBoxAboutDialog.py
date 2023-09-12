
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt, Slot, QCoreApplication
from .ui_forms.ui_DialogAbout import Ui_Dialog
import webbrowser



class UBoxAboutDialog(QDialog):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #init buttons
        self.ui.btn_python3.clicked.connect(self._on_link_btn)
        self.ui.btn_pyside6.clicked.connect(self._on_link_btn)
        self.ui.btn_developerwebsite.clicked.connect(self._on_link_btn)
        self.ui.btn_support_author.clicked.connect(self._on_link_btn)

    def set_version(self, t:tuple):
        self.ui.version_label.setText(self.ui.version_label.text() + str(t))

    @Slot()
    def _on_link_btn(self):
        web_link = ""
        match self.sender():
            case self.ui.btn_python3:
                web_link = r"https://www.python.org"
            case self.ui.btn_pyside6:
                web_link = r"https://doc.qt.io/qtforpython-6/index.html"
            case self.ui.btn_developerwebsite:
                web_link = r"https://www.ironmesh.ru"
            case self.ui.btn_support_author:
                web_link = r"https://ironmesh.ru/other/support-projects"

        webbrowser.open_new_tab(web_link)






