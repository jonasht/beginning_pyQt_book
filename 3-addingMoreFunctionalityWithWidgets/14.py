# setting up the window for the long gui

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox


from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
from registration import NewUserDialog


class LoginWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setFixedSize(360, 220)
        self.setWindowTitle('login')

        self.setUpWindow()
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    
    sys.exit(app.exec())
    