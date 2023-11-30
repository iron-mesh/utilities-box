import os

from PySide6.QtWidgets import QListWidget, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QSpacerItem ,QSizePolicy, QInputDialog, QListWidgetItem, QLineEdit, QFileDialog, QMessageBox, QApplication
from PySide6.QtCore import Signal, Slot, QCoreApplication, Qt, QSize
from . import PathInputMode
import logging



class NamedFilePathListInput(QWidget):
    """Widget for input of list of pathes(file or directory). List items has unique names and pathes only"""

    def __init__(self, mode:PathInputMode=PathInputMode.Directory, parent=None):
        super().__init__(parent)
        self.set_mode(mode)
        self._file_filter = "(*.*)"

        verticalLayout_3 = QVBoxLayout(self)
        horizontalLayout_2 = QHBoxLayout()
        verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self._listWidget = QListWidget()
        self._listWidget.setFont(QApplication.font())
        self._listWidget.currentRowChanged.connect(self._on_currentrow_changed)
        self._listWidget.itemChanged.connect(self._on_name_changed)
        self._listWidget.setMinimumSize(QSize(0, 150))

        horizontalLayout_2.addWidget(self._listWidget)
        verticalLayout = QVBoxLayout()

        self.add_btn = QPushButton("+")
        self.add_btn.clicked.connect(self._on_add_btn)
        verticalLayout.addWidget(self.add_btn)

        self.del_btn = QPushButton("-")
        self.del_btn.clicked.connect(self._on_del_btn)
        verticalLayout.addWidget(self.del_btn)

        verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        verticalLayout.addItem(verticalSpacer)

        horizontalLayout_2.addLayout(verticalLayout)
        verticalLayout_3.addLayout(horizontalLayout_2)

        horizontalLayout = QHBoxLayout()

        self.path_lineEdit = QLineEdit()
        self.path_lineEdit.setEnabled(False)
        horizontalLayout.addWidget(self.path_lineEdit)

        self.select_btn = QPushButton("...")
        self.select_btn.clicked.connect(self._on_select_btn)
        horizontalLayout.addWidget(self.select_btn)

        verticalLayout_3.addLayout(horizontalLayout)


    def get_list(self) -> list[tuple]:
        """Return tuple: (<Item Name>, <Path>)"""
        extracted_list: list[tuple] = []
        for i in range(self._listWidget.count()):
            item = self._listWidget.item(i)
            name = item.text()
            path = item.data(Qt.ItemDataRole.UserRole)
            extracted_list.append((name, path))
        return extracted_list

    def set_list(self, lst: list[tuple]) -> None:
        """Set list of items"""
        self._listWidget.clear()
        for i in lst:
            name = i[0]
            path = i[1]
            if not self._is_itempart_unique(path, part="p"): continue
            item = QListWidgetItem(self._validate_item_name(name))
            item.setData(Qt.ItemDataRole.UserRole, path)
            item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable)
            self._listWidget.addItem(item)

    def setToolTip(self, arg__1: str) -> None:
        self._listWidget.setToolTip(arg__1)

    def toolTip(self) -> str:
        return self._listWidget.toolTip()

    def set_mode(self, mode: PathInputMode) -> None:
        """Set mode of input: file selection, directory selections"""
        if mode == PathInputMode.FileSave:
            raise ValueError("This widget doesn't support <FileSave> mode")
        self._mode = mode

    def mode(self) -> PathInputMode:
        """Returns mode of input"""
        return self._mode

    def set_file_filter(self, filter: str = "(*.*)") -> None:
        """Set file extensions filter
                For example: Sound, (*.mp3)"""
        self._file_filter = filter

    def file_filter(self) -> str:
        """Return file filter
        For example: (Sound, (*.mp3))"""
        return self._file_filter

    def _is_itempart_unique(self, text:str, ignore_row:int=-1, part:str="n") -> bool:
        """Check unique of item part
        part options:
            n - name
            p - path"""
        for i in range(self._listWidget.count()):
            if i == ignore_row: continue
            item = self._listWidget.item(i)
            check_text = item.text() if part == "n" else item.data(Qt.ItemDataRole.UserRole)
            if text == check_text:
                return False
        return True

    def _get_path(self) -> str:
        prev_path = self.path_lineEdit.text()
        path: str = ""
        if (self._mode == PathInputMode.Directory):
            path: str = QFileDialog.getExistingDirectory(None, QCoreApplication.translate("input_widgets", "Select Folder"), prev_path,
                                                         QFileDialog.ShowDirsOnly)
        elif (self._mode == PathInputMode.FileOpen):
            path: str = QFileDialog.getOpenFileName(None, QCoreApplication.translate("input_widgets", "Select File"), prev_path, self.file_filter())[0]

        return path

    @Slot()
    def _on_add_btn(self):
        path = self._get_path()
        if os.path.exists(path):
            name = os.path.basename(path)
            if self._is_itempart_unique(path, part="p"):
                item = QListWidgetItem()
                item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable)
                item.setText(self._validate_item_name(name))
                item.setData(Qt.ItemDataRole.UserRole, path)
                self._listWidget.addItem(item)
            else:
                mes = QCoreApplication.translate("input_widgets", "Path: <{0}> already exists").format(path)
                QMessageBox.warning(self, QCoreApplication.translate("input_widgets", "Warning"), mes)

    @Slot()
    def _on_select_btn(self):
        row = self._listWidget.currentRow()
        if row >= 0:
            self._listWidget.blockSignals(True)
            item = self._listWidget.item(row)
            path = self._get_path()
            if self._is_itempart_unique(path, row, "p"):
                item.setData(Qt.ItemDataRole.UserRole, path)
                self.path_lineEdit.setText(item.data(Qt.ItemDataRole.UserRole))
            else:
                mes = QCoreApplication.translate("input_widgets", "Path: <{0}> already exists").format(path)
                QMessageBox.warning(self, QCoreApplication.translate("input_widgets", "Warning"), mes)
            self._listWidget.blockSignals(False)

    def _validate_item_name(self, name:str, ignore_row:int=-1) -> str:
        """Returns modified <name> if it's not unique, otherwise - original <name>"""
        i = 2
        new_name = QCoreApplication.translate("input_widgets", "Unnamed") if name == "" else name
        orig_name = new_name
        while not self._is_itempart_unique(new_name, ignore_row, part="n"):
            new_name = f"{orig_name} ({i})"
            i += 1
        return new_name

    @Slot(QListWidgetItem)
    def _on_name_changed(self, item:QListWidgetItem):
        name = item.text()
        logging.debug(f"in <_on_name_changed> name: {name}")
        self._listWidget.blockSignals(True)
        item.setText(self._validate_item_name(name, self._listWidget.row(item)))
        self._listWidget.blockSignals(False)

    @Slot()
    def _on_del_btn(self):
        row = self._listWidget.currentRow()
        if row >= -1:
            self._listWidget.takeItem(row)
            if self._listWidget.count() == 0:
                self.path_lineEdit.clear()

    @Slot(int)
    def _on_currentrow_changed(self, row:int):
        logging.debug(f" in _on_currentrow_changed, row {row} ")
        if row > -1:
            path = self._listWidget.item(row).data(Qt.ItemDataRole.UserRole)
            self.path_lineEdit.setText(path)


