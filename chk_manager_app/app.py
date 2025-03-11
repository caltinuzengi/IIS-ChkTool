import sys
import os
import shutil
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
                             QCheckBox, QMessageBox, QScrollArea, QHBoxLayout)
from config import ROOT_DIR

services = {}

class ServiceManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadServices()

    def initUI(self):
        self.setWindowTitle('Chk Manager')
        self.layout = QVBoxLayout()

        self.scroll = QScrollArea()
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout()

        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll.setWidget(self.scroll_widget)
        self.scroll.setWidgetResizable(True)
        self.layout.addWidget(self.scroll)

        self.button_layout = QHBoxLayout()
        self.off_button = QPushButton('OFF Selected')
        self.live_button = QPushButton('LIVE Selected')
        self.rollback_button = QPushButton('Rollback')
        self.refresh_button = QPushButton('Refresh')

        self.off_button.clicked.connect(lambda: self.updateSelected('off'))
        self.live_button.clicked.connect(lambda: self.updateSelected('live'))
        self.rollback_button.clicked.connect(self.rollbackSelected)
        self.refresh_button.clicked.connect(self.loadServices)

        self.button_layout.addWidget(self.off_button)
        self.button_layout.addWidget(self.live_button)
        self.button_layout.addWidget(self.rollback_button)
        self.button_layout.addWidget(self.refresh_button)

        self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)

    def loadServices(self):
        while self.scroll_layout.count():
            child = self.scroll_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        global services
        services.clear()

        def add_service(chk_path, service_name):
            with open(chk_path, "r") as f:
                status = f.read().strip().lower()
            services[service_name] = {"status": status, "path": chk_path}
            if not os.path.exists(chk_path + ".bak"):
                shutil.copy(chk_path, chk_path + ".bak")

            h_layout = QHBoxLayout()
            checkbox = QCheckBox(service_name)
            label = QLabel(f"Status: {status.upper()} | Path: {chk_path}")
            h_layout.addWidget(checkbox)
            h_layout.addWidget(label)
            self.scroll_layout.addLayout(h_layout)
            services[service_name]["checkbox"] = checkbox

        for subdir, dirs, files in os.walk(ROOT_DIR):
            if "chk.txt" in files:
                chk_path = os.path.join(subdir, "chk.txt")
                service_name = os.path.basename(subdir)
                add_service(chk_path, service_name)

            if "chk" in dirs:
                chk_sub_path = os.path.join(subdir, "chk", "chk.txt")
                if os.path.exists(chk_sub_path):
                    service_name = os.path.basename(subdir)
                    add_service(chk_sub_path, service_name)

    def updateSelected(self, status):
        for svc, info in services.items():
            if info["checkbox"].isChecked():
                with open(info["path"], "w") as f:
                    f.write(status)
        QMessageBox.information(self, "Succesfull", f"Selected Services: '{status}'")
        self.loadServices()

    def rollbackSelected(self):
        for svc, info in services.items():
            if info["checkbox"].isChecked():
                bak_path = info["path"] + ".bak"
                if os.path.exists(bak_path):
                    shutil.copy(bak_path, info["path"])
        QMessageBox.information(self, "Rollback", "Rollback Completed for Selected Services")
        self.loadServices()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ServiceManager()
    ex.show()
    sys.exit(app.exec_())