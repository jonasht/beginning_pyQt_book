# code for clearText() and accepttext() slots




import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

from PyQt6.QtCore import Qt





class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # self.setGeometry(100, 100, 550, 250)
        self.setMaximumSize(510, 230)
        self.setWindowTitle('QlineEdit')


        self.setUpMainWindow()
        self.show()
    def setUpMainWindow(self):
        QLabel('please enter your name below/ por favor entre com seu nome abaixo',self).move(70, 70)
        name_lb = QLabel('name:', self)
        name_lb.move(20, 50)

        self.name_edit = QLineEdit(self)
        self.name_edit.resize(210, 20)
        self.name_edit.move(70, 50)

        self.clear_bt = QPushButton('clear', self)
        self.clear_bt.move(140, 90)
        self.clear_bt.clicked.connect(self.clearText)

        self.acceptText_bt = QPushButton('accept', self)
        self.acceptText_bt.move(210, 90)
        self.acceptText_bt.clicked.connect(self.acceptText)
        
    def clearText(self):
        self.name_edit.clear()

    def acceptText(self):
        print(self.name_edit.text())
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    