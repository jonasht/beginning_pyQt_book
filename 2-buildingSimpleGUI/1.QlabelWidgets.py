import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initalizeUI()
        
    def initalizeUI(self):
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle('window')
        
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        hello_lb = QLabel(self)
        hello_lb.setText('hello/olah')
        hello_lb.move(105, 15)
        
        image = './images/world.png'

        try:
            with open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
        except FileNotFoundError as error:
            print(f'image not found.\n error: {error}')
            print('imagem nao encontrada')

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

