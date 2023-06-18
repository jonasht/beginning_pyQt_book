import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap

__main__ = '__main__'



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initializeUI()
    
    def initializeUI(self):
        self.setGeometry(50, 80, 250, 400)
        self.setWindowTitle('profile')

        self.setUpWindow()

        self.show()

    def createImageLabels(self):
        images = ['./images/skyblue.png', './images/profile_image.png']

        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    if image == './images/profile_image.png':
                        label.move(80, 20)
            except FileNotFoundError as error:
                print(f'image not found {error}')
                print('image nao encontrada')

    def setUpWindow(self):
        self.createImageLabels()
        
        user_label = QLabel(self)        
        user_label.setText('John Teixeira')
        user_label.setFont(QFont('Arial', 20))
        user_label.move(85, 140)

        bio_label = QLabel(self)
        bio_label.setText('Biography')
        bio_label.setFont(QFont('Arial', 17))

        bio_label.move(15, 170)

        about_label = QLabel(self)
        about_label.setText('I\'m a software engineer with 4 years experience creating awesome codes.')
        about_label.setWordWrap(True)
        about_label.move(15, 190)
        
if __name__ == __main__:
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
    
    