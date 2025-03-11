# # Kök dizin (chk.txt dosyalarının bulunduğu yer)
# ROOT_DIR = r"C:\inetpub\wwwroot"  # Burayı kendi path'inize göre güncelleyebilirsiniz

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QRadioButton, QLineEdit, QPushButton, QLabel, QHBoxLayout

class RootSelector(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.selected_path = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Select Root Directory")
        layout = QVBoxLayout()

        self.radio1 = QRadioButton("C:\\inetpub\\wwwroot")
        self.radio2 = QRadioButton("C:\\Ecommerce")
        self.radio_custom = QRadioButton("Other:")
        self.custom_path = QLineEdit()

        layout.addWidget(QLabel("Select root directory:"))
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.radio_custom)
        h_layout.addWidget(self.custom_path)
        layout.addLayout(h_layout)

        self.continue_button = QPushButton("Continue")
        self.continue_button.clicked.connect(self.setPath)

        layout.addWidget(self.continue_button)
        self.setLayout(layout)

    def setPath(self):
        if self.radio1.isChecked():
            self.selected_path = "C:\\inetpub\\wwwroot"
        elif self.radio2.isChecked():
            self.selected_path = "C:\\Ecommerce"
        elif self.radio_custom.isChecked():
            self.selected_path = self.custom_path.text().strip()
        self.accept()