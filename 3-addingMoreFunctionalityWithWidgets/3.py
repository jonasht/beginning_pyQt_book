# code for teh buttonclicked () slot

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt





class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 550, 250)
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

    def buttonClicked(self):
        self.time_pressed +=1
        if self.time_pressed ==1:
            self.name_lb.setText('why d you press me? por que me apertarias')
        if self.time_pressed ==2:
            self.name_lb.setText('I\'m warning you/ estou te avisando')
            self.bt.setText('feelin lucky?/sentindo se com sorte')
            self.bt.adjustSize()
            self.bt.move(70, 70)

        if self.time_pressed == 3:
            print('the window has been closed/ a janela foi fechada')
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    