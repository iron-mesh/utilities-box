import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QLineEdit, QFormLayout
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Folder Creator")
        self.setMinimumWidth(400)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout(main_widget)
        layout.addWidget(QLabel("Select the location to create the folder:"))

        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        self.selected_folder_label = QLabel()
        button_layout.addWidget(self.selected_folder_label)

        select_folder_button = QPushButton("Select Folder")
        select_folder_button.clicked.connect(self.select_folder)
        button_layout.addWidget(select_folder_button)

        form_layout = QFormLayout()
        layout.addLayout(form_layout)

        self.folder_structure_input = QLineEdit()
        form_layout.addRow("Folder Structure:", self.folder_structure_input)

        create_folder_button = QPushButton("Create Folder")
        create_folder_button.clicked.connect(self.create_folder)
        layout.addWidget(create_folder_button)

    def select_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        selected_folder = QFileDialog.getExistingDirectory(self, "Select Directory", options=options)
        self.selected_folder_label.setText(selected_folder)

    def create_folder(self):
        selected_folder = self.selected_folder_label.text()
        folder_structure = self.folder_structure_input.text()

        folder_names = folder_structure.split("/")
        folder_path = selected_folder
        for folder_name in folder_names:
            folder_path = os.path.join(folder_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
