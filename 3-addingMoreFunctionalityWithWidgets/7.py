# setting up the main window or using qcheckbox widgets


import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QLabel

from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle('qcheckbox')

        self.setUpMainWindow()
        self.show()

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    sys.exit(app.exec())

    