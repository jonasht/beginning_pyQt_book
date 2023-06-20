from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QLineEdit, QPushButton
import sys
from PyQt6.QtGui import QFont



class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 340, 140)
        self.setWindowTitle('messagebox')

        self.setUpMainWindow()
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

    