from PySide2.QtWidgets import QHBoxLayout, QWidget, QLineEdit, QPushButton, QFileDialog
from PySide2.QtCore import Signal
import logging, enum

logging.basicConfig(level=logging.DEBUG)


@enum.unique
class PathInputMode(enum.IntEnum):
    FileOpen = 0
    Directory = 1
    FileSave = 2


class PathInput(QWidget):
    """Widget for input of path to a file or a directory"""

    path_changed = Signal(str)

    def __init__(self, parent=None, mode: PathInputMode = PathInputMode.FileOpen):
        super().__init__(parent)
        self._mode = mode
        self._title: str = ""
        self._file_filter: str = ""
        self._placeholder: str = ""

        self._line_edit = QLineEdit()
        self._btn_selectpath = QPushButton(u"...")
        self._btn_selectpath.clicked.connect(self._on_select_path)
        self._btn_clear = QPushButton(u"✖")
        self._btn_clear.clicked.connect(self._on_clear)

        layout = QHBoxLayout(self)
        layout.setMargin(0)
        layout.addWidget(self._line_edit)
        layout.addWidget(self._btn_selectpath)
        layout.addWidget(self._btn_clear)

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

    def get_path(self) -> str:
        """Get path to a file|directory"""
        return self._line_edit.text()

    def set_path(self, path: str) -> None:
        """Set path to a file|directory"""
        return self._line_edit.setText(path)

    def set_file_filter(self, filter: str = "(*.*)") -> None:
        """Set file extensions filter (filter label and filter)
                For example: Sound, (*.mp3)"""
        self._file_filter = filter

    def file_filter(self) -> str:
        """Return Tuple(filter label, filter)
        For example: (Sound, (*.mp3))"""
        return self._file_filter

    def set_placeholder(self, s: str) -> None:
        """Set placeholder text of text field"""
        self._line_edit.setPlaceholderText(s)

    def placeholder(self) -> str:
        """Get placeholder text of text field"""
        return self._line_edit.placeholderText()

    def setToolTip(self, arg__1: str) -> None:
        self._line_edit.setToolTip(arg__1)

    def toolTip(self) -> str:
        return self._line_edit.toolTip()

    def _on_select_path(self) -> None:
        buf_path = self.get_path()
        path: str = ""
        if (self._mode == PathInputMode.Directory):
            path: str = QFileDialog.getExistingDirectory(None, self.window_title(), self.get_path(),
                                                         QFileDialog.ShowDirsOnly)
        elif (self._mode == PathInputMode.FileOpen):
            path: str = QFileDialog.getOpenFileName(None, self.window_title(), self.get_path(),
                                                    f"{self.file_filter()[0]} {self.file_filter()[1]}")[0]
        elif (self._mode == PathInputMode.FileSave):
            path: str = QFileDialog.getSaveFileName(None, self.window_title(), self.get_path(),
                                                    f"{self.file_filter()[0]} {self.file_filter()[1]}")[0]

        if (path != buf_path and path):
            self.set_path(path)
            self.path_changed.emit(path)

    def _on_clear(self) -> None:
        self._line_edit.clear()
