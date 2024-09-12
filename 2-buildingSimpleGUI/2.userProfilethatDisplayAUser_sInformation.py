import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initializeUI()
    
    def initializeUI(self):
        self.setGeometry(50, 50, 250, 400)
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
        
        # user label 
        user_label = QLabel(self)        
        user_label.setText('John Ter')
        user_label.setFont(QFont('Arial', 17))
        user_label.move(85, 140)

        # bio label
        bio_label = QLabel(self)
        bio_label.setText('Biography')
        bio_label.setFont(QFont('Arial', 17))
        bio_label.move(15, 170)
        
        # about label
        about_label = QLabel(self)
        about_label.setText('I\'m a software engineer with 4 years\nexperience creating awesome codes.')
        about_label.setWordWrap(True)
        about_label.move(15, 190)
        
        # skill label
        skill_label = QLabel(self)
        skill_label.setText('Skill')
        skill_label.setFont(QFont('Arial', 17))
        skill_label.move(15,240)

        language_label = QLabel(self)
        language_label.setText('Python |Tkinter| SQL | JavaScript')
        language_label.move(15,260)

        experience_label = QLabel(self)
        experience_label.setText('Experience')
        experience_label.setFont(QFont('Arial', 17))
        experience_label.move(15, 290)

        dev_label = QLabel(self)
        dev_label.setText('Python Developer')
        dev_label.move(15,310)

        devDates_label = QLabel(self)
        devDates_label.setText('Jar 2011 - Present')
        devDates_label.setFont(QFont('Arial', 10))
        devDates_label.move(15,330)

        driver_label = QLabel(self)
        driver_label.setText('pizza delivery driver'.title())
        driver_label.move(15,350)

        driverDates_label = QLabel(self)
        driverDates_label.setText('aug 2015 - dec 2018'.title())
        driverDates_label.setFont(QFont('Arial', 10))
        driverDates_label.move(15,370)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
    
    