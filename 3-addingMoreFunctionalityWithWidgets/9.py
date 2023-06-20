# code for the printselected() slot


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
        
    def setUpMainWindow(self):
        header_lb = QLabel('which shifts can you work? \ (please check all apply)', self)
        header_lb.setWordWrap(True)
        header_lb.move(20, 10)

        morning_cb = QCheckBox('8 am red', self)
        morning_cb.move(40, 60)
        morning_cb.toggle()
        morning_cb.toggled.connect(self.printSelected)

        after_cb = QCheckBox('afternoon 1 pm 8 pm', self)
        after_cb.move(40, 80)
        after_cb.toggled.connect(self.printSelected)

        night_cb = QCheckBox('night 7 pm 3 am ', self)
        night_cb.move(40, 100)
        night_cb.toggled.connect(self.printSelected)

    def printSelected(self, checked): 
        sender = self.sender()
        if checked:
            print(f'{sender.text()} selected')
        else:
            print(f'{sender.text()} Deselected')
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

    