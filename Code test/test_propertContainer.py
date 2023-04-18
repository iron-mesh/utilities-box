import sys, os

from PySide2.QtWidgets import QWidget,QApplication,QVBoxLayout,QScrollArea, QPushButton
from PySide2.QtGui import QFont
from Code.PyUB.Types import PropertyContainer
from Code.PyUB.Types.InputWidgets import PathInputMode
from Code.PyUB.Types.Properties import *

class Settings(PropertyContainer):
    string: StringProperty(default_value="LongLongLongLongLongLongLongLongLongLongLongText", name="Just Text", placeholder="here any text", tool_tip="Здесь могла быть полезная подсказка")

    string1: StringProperty(name="Just Another Text", placeholder="here any text", tool_tip="Здесь могла быть полезная подсказка", maxlen= 7)



    size:IntProperty(name="Just a number", default_value=5, maximum=99999999, tool_tip="Здесь могла быть полезная подсказка")





    Nfloat: FloatProperty(name="Just a Float number", default_value= 60, maximum=1000.0, minimum=-1000.0, tool_tip="Здесь могла быть полезная подсказка")
    boolean2: BoolProperty(default_value=True, name="Another Checkbox", tool_tip="Здесь могла быть полезная подсказка")
    pfile:FilePathProperty(name ="Выбери mp3 файл", mode = PathInputMode.FileOpen, dialog_title ="Открыть mp3 файл", tool_tip ="Здесь могла быть полезная подсказка")
    dfile: FilePathProperty(name="Выбери папку", mode=PathInputMode.Directory, dialog_title="Выбрать папку", tool_tip="Здесь могла быть полезная подсказка")
    filesave: FilePathProperty(name="Файл сохранения", mode=PathInputMode.FileSave, dialog_title="Файл сохранения", filter="(*.mp3 *.mp2)", tool_tip="Здесь могла быть полезная подсказка")
    string_list:StringListProperty(name="Список строк", default_value=["Hello", "World", "Just"], tool_tip="It's toll tip")
    cbox:ComboBoxProperty(name="Напиток", items=["Кофе","Чай","Сок","Кофе в арбузной оболочке"], default_value=-1)
    file_list: FilePathListProperty(name="File list", mode=PathInputMode.FileOpen, )
    dir_list: FilePathListProperty(name="Dir list", mode=PathInputMode.Directory)
    ufile_list: FilePathListProperty(name="File list (Unique)", mode=PathInputMode.FileOpen, unique_only=True)
    udir_list: FilePathListProperty(name="Dir list (Unique)", mode=PathInputMode.Directory, unique_only=True)
    font:FontSelectProperty(name="Выбор шрифта")
    paswrd:PasswordStringProperty(name="Пароль")




def print_settings():
    print(Settings.encode_json())

def print_settings_updated():
    print ("data has been updated" if Settings.update_data() else "data has been NOT updated")
    print(Settings.encode_json())


app = QApplication(sys.argv)
app.setFont(QFont("Arial", 12, QFont.Normal))
app.setStyle("Fusion")
window = QWidget()
window.setWindowTitle("PropertyContainer Test")
window.resize(1000, 500)
scroll_area = QScrollArea()
layout = QVBoxLayout(window)
layout.addWidget(Settings.render_layout2())
# scroll_area.setWidget(Settings.render_layout())
btn = QPushButton("Print Properties")
btn.clicked.connect(print_settings)
btn2 = QPushButton("Update Print Properties")
btn2.clicked.connect(print_settings_updated)
layout.addWidget(btn)
layout.addWidget(btn2)
window.show()
sys.exit(app.exec_())