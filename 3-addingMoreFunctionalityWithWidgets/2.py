# the setUpmainwindow() mothded for using buttons

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle('QpushButton')

        self.setUpMainWindow()
        self.show()
    def setUpMainWindow(self):
        self.time_pressed = 0
        
        self.name_lb = QLabel('dont push the button/ nao aperto o botao', self)
        self.name_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_lb.move(60, 30)

        self.bt = QPushButton('push me/ aperta me', self)
        self.bt.move(80, 70)
        self.bt.clicked.connect(self.buttonClicked)

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    