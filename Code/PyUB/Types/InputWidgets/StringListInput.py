
from PySide2.QtWidgets import QListWidget, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QSpacerItem ,QSizePolicy, QInputDialog, QListWidgetItem
from PySide2.QtCore import Signal, Slot, QCoreApplication
import logging

logging.basicConfig(level=logging.DEBUG)



class StringListInput(QWidget):
    """Widget for input of list of strings"""


    def __init__(self, parent = None):
        super().__init__(parent)
        horizontalLayout = QHBoxLayout(self)

        self.listWidget = QListWidget()

        self.listWidget.itemDoubleClicked.connect(self._edit_item)
        horizontalLayout.addWidget(self.listWidget)
        horizontalLayout.setMargin(0)

        verticalLayout = QVBoxLayout()

        add_btn = QPushButton("+")
        add_btn.clicked.connect(self._add_item)
        verticalLayout.addWidget(add_btn)

        edit_btn = QPushButton("✎")
        edit_btn.clicked.connect(self._edit_item)
        verticalLayout.addWidget(edit_btn)

        delete_btn = QPushButton("−")
        delete_btn.clicked.connect(self._del_item)
        verticalLayout.addWidget(delete_btn)

        verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)
        verticalLayout.addItem(verticalSpacer_2)

        moveup_btn = QPushButton("⮝")
        moveup_btn.clicked.connect(lambda :self._move_item("up"))
        verticalLayout.addWidget(moveup_btn)

        movedown_btn = QPushButton("⮟")
        movedown_btn.clicked.connect(lambda: self._move_item("down"))
        verticalLayout.addWidget(movedown_btn)

        verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        verticalLayout.addItem(verticalSpacer)
        horizontalLayout.addLayout(verticalLayout)


    def get_list(self) -> list[str]:
        """Get list"""
        extracted_list: list[str] = []
        for i in range(self.listWidget.count()):
            extracted_list.append(self.listWidget.item(i).text())
        return extracted_list

    def set_list(self, lst: list[str]) -> None:
        """Set list"""
        self.listWidget.clear()
        self.listWidget.addItems(lst)

    def setToolTip(self, arg__1:str) -> None:
        self.listWidget.setToolTip(arg__1)

    def toolTip(self) -> str:
        return self.listWidget.toolTip()

    @Slot()
    def _add_item(self):
        text, ok = QInputDialog.getText(self, QCoreApplication.translate("input_widgets", "Add string"),
                                        QCoreApplication.translate("input_widgets", "Enter the line text"))
        if ok and text:
            self.listWidget.addItem(text)

    @Slot()
    def _edit_item(self):
        row = self.listWidget.currentRow()
        item: QListWidgetItem = self.listWidget.item(row)

        text, ok = QInputDialog.getText(self, QCoreApplication.translate("input_widgets", "Edit string"),
                                        QCoreApplication.translate("input_widgets", "Edit the line text"),
                                        text=item.text())

        if ok and text:
            item.setText(text)

    @Slot()
    def _del_item(self):
        row = self.listWidget.currentRow()
        self.listWidget.takeItem(row)

    @Slot()
    def _move_item(self, direction: str):
        row = self.listWidget.currentRow()
        count = self.listWidget.count()

        if direction == "up":
            if row > 0:
                item = self.listWidget.takeItem(row)
                self.listWidget.insertItem(row - 1, item)
                self.listWidget.setCurrentRow(row - 1)

        elif direction == "down":
            if row < count - 1:
                item = self.listWidget.takeItem(row)
                self.listWidget.insertItem(row + 1, item)
                self.listWidget.setCurrentRow(row + 1)