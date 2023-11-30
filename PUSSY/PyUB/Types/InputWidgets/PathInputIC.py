from PySide6.QtWidgets import QLineEdit, QFileDialog
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QIcon
from . import PathInputMode
from PyUB.App import pussy_ressources_rc



class PathInputIC(QLineEdit): # унаследовать от лайнэдит
    """Widget for input of path to a file or a directory"""

    path_changed = Signal(str)

    def __init__(self, parent=None, mode: PathInputMode = PathInputMode.FileOpen):
        super().__init__(parent)
        self._mode = mode
        self._title: str = "Open|Save file/folder"
        self._file_filter: str = "(*.*)"
        self._placeholder: str = ""
        self._is_empty = True

        self._action = self.addAction(QIcon(":/icons/icons/open_folder.png"), QLineEdit.TrailingPosition)
        self._action.triggered.connect(self._on_action)
        self.textChanged.connect(self._on_text_changed)


    def set_mode(self, mode: PathInputMode) -> None:
        """Set mode of input: file selection, directory selections, file_saving"""
        self._mode = mode

    def mode(self) -> PathInputMode:
        """Get mode of input"""
        return self._mode

    def set_window_title(self, title: str) -> None:
        """Set title of file select dialog window"""
        self._title = title

    def window_title(self) -> str:
        """Get title of file select dialog window"""
        return self._title

    def path(self) -> str:
        """Get path to a file|directory"""
        return self.text()

    def set_path(self, path: str) -> None:
        """Set path to a file|directory"""
        return self.setText(path)

    def set_file_filter(self, filter: str = "(*.*)") -> None:
        """Set file extensions filter (filter label and filter)
                For example: Sound, (*.mp3)"""
        self._file_filter = filter

    def file_filter(self) -> str:
        """Return Tuple(filter label, filter)
        For example: (Sound, (*.mp3))"""
        return self._file_filter

    @Slot()
    def _on_action(self) -> None:
        if self._is_empty:
            prev_path = self.path()
            path: str = ""
            if (self._mode == PathInputMode.Directory):
                path: str = QFileDialog.getExistingDirectory(None, self.window_title(), self.path(),
                                                             QFileDialog.ShowDirsOnly)
            elif (self._mode == PathInputMode.FileOpen):
                path: str = QFileDialog.getOpenFileName(None, self.window_title(), self.path(), self.file_filter())[0]
            elif (self._mode == PathInputMode.FileSave):
                path: str = QFileDialog.getSaveFileName(None, self.window_title(), self.path(), self.file_filter())[0]

            if (path != prev_path and path):
                self.set_path(path)
                self.path_changed.emit(path)
        else:
            self.clear()


    @Slot(str)
    def _on_text_changed(self, text:str) -> None:
        if self._is_empty and text:
            self._is_empty = False
            self._action.setIcon(QIcon(":/icons/icons/delete.png"))
        elif not self._is_empty and not text:
            self._is_empty = True
            self._action.setIcon(QIcon(QIcon(":/icons/icons/open_folder.png")))
