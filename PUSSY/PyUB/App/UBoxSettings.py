
from ..Types.Properties import *
from ..Types import PropertyContainer
from ..Types.InputWidgets import PathInputMode

from PySide6.QtWidgets import QWidget, QHBoxLayout, QListWidget, QScrollArea, QStackedWidget, QFormLayout, QAbstractScrollArea, QLabel, QApplication, QSizePolicy
from PySide6.QtCore import Qt, Slot, QCoreApplication

class UBoxSettings(PropertyContainer):
    style: ComboBoxProperty(items=["MacOS", "Fusion", "Windows", "WindowsVista"], default_value=0, name="Theme")
    font_size: IntProperty(name="Font size", default_value=10, minimum=8, maximum=48)
    font_family:FontSelectProperty(name="Font")
    show_error_msg:BoolProperty(False, "Display error info in Logs")
    external_plugin_dir:NamedFilePathListProperty(name="External plugin directories", mode=PathInputMode.Directory)

    @classmethod
    def render_layout(cls) -> QWidget:
        @Slot(int)
        def on_row_changed(row:int):
            nonlocal pages
            pages.setCurrentIndex(row)

        widget = QWidget()
        main_layout = QHBoxLayout(widget)

        chapter_list = QListWidget()
        cls._chapter_list = chapter_list
        chapter_list.setFont(QApplication.font())
        chapter_list.currentRowChanged.connect(on_row_changed)
        chapter_list.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        chapter_list.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding))
        main_layout.addWidget(chapter_list)

        pages = QStackedWidget()
        main_layout.addWidget(pages)

        props_distr_list = [("Interface", ["style", "font_family", "font_size", "show_error_msg"]),
                            ("Additional Plugin Dirs", ["external_plugin_dir"])]
        cls._lable_list = {}
        for chapter, prop_list in props_distr_list:
            chapter_list.addItem(chapter)
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            widget_content = QWidget()
            layout = QFormLayout(widget_content)
            layout.setVerticalSpacing(15)
            layout.setLabelAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            row: int = 0
            for key in prop_list:
                prop = cls.get_property(key)
                cls._lable_list[key] = QLabel(prop.get_name())
                cls._lable_list[key].setWordWrap(True)
                layout.setWidget(row, QFormLayout.LabelRole, cls._lable_list[key])
                layout.setWidget(row, QFormLayout.FieldRole, prop.get_input_widget())
                row += 1
            scroll_area.setWidget(widget_content)
            pages.addWidget(scroll_area)
        chapter_list.setCurrentRow(0)
        return widget

    def retranslate(cls) -> None:
        super().retranslate()
        for i in range(cls._chapter_list.count()):
            text = QCoreApplication.translate("settings", cls._chapter_list.item(i).text())
            cls._chapter_list.item(i).setText(text)



