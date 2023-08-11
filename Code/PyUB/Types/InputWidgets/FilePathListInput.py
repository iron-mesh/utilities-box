
from PySide6.QtWidgets import QInputDialog, QListWidgetItem, QFileDialog
from PySide6.QtCore import Signal, Slot, QCoreApplication
from . import StringListInput
from .PathInput import PathInputMode
import logging

logging.basicConfig(level=logging.DEBUG)



class FilePathListInput(StringListInput):
    """Widget for input of list of file or directory path"""


    def __init__(self, parent = None, mode: PathInputMode = PathInputMode.Directory):
        super().__init__(parent)
        self._mode = mode
        self._file_filter: str = ""
        self._unique_only: bool = False

    def set_mode(self, mode:PathInputMode) -> None:
        """Set mode of input: file selection, directory selections"""
        self._mode = mode

    def mode(self)->PathInputMode:
        """Return input mode (file selection, directory selections)"""
        return self._mode

    def set_file_filter(self, filter: str = "(*.*)") -> None:
        """Set file extensions filter (filter label and filter)
                For example: Sound, (*.mp3)"""
        self._file_filter = filter

    def file_filter(self) -> str:
        """Return file filter
        For example: (Sound, (*.mp3))"""
        return (self._file_filter)

    @property
    def unique_only(self) -> bool:
        return self._unique_only

    @ unique_only.setter
    def unique_only(self, value) -> None:
        self._unique_only = value

    @Slot()
    def _add_item(self):
        path: str = ""
        if (self._mode == PathInputMode.Directory):
            path: str = QFileDialog.getExistingDirectory(None, QCoreApplication.translate("input_widgets", "Select Existing File"), "",
                                                         QFileDialog.ShowDirsOnly)
        elif (self._mode == PathInputMode.FileOpen):
            path: str = QFileDialog.getOpenFileName(None, QCoreApplication.translate("input_widgets", "Select Existing Directory"), "", self.file_filter())[0]
        if path and not(self._path_is_exist(path) and self.unique_only):
            self.listWidget.addItem(path)

    @Slot()
    def _edit_item(self):
        path: str = ""
        row = self.listWidget.currentRow()
        item: QListWidgetItem = self.listWidget.item(row)
        if (self._mode == PathInputMode.Directory):
            path: str = QFileDialog.getExistingDirectory(None, QCoreApplication.translate("input_widgets", "Select Existing File"), item.text(), QFileDialog.ShowDirsOnly)
        elif (self._mode == PathInputMode.FileOpen):
            path: str = QFileDialog.getOpenFileName(None, QCoreApplication.translate("input_widgets", "Select Existing Directory"), item.text(), self.file_filter())[0]

        if path and not(self._path_is_exist(path) and self.unique_only):
            item.setText(path)

    @Slot()
    def _del_item(self):
        row = self.listWidget.currentRow()
        self.listWidget.takeItem(row)

    def _path_is_exist(self, path) -> bool:
        for row in range(self.listWidget.count()):
            if path == self.listWidget.item(row).text():
                return True
        return False

