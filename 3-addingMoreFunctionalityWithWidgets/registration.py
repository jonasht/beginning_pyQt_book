
import sys
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtGui import QFont, QPixmap


class NewUserDialog(QDialog):
    def __init__(self) -> None:
        super().__init__()

        self.setModal(True)
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(360, 320)
        self.setWindowTitle('registration gui')
        self.setUpWindow()

    def setUpWindow(self):
        lb_login = QLabel('create a new account', self)
        lb_login.setFont(QFont('Arial', 20))
        lb_login.move(90, 20)

        user_image = 'images/new_user_icon.png'
        try:
            with open(user_image):
                lb_user = QLabel(self)
                pixmap = QPixmap(user_image)
                lb_user.move(150, 60)
        except FileNotFoundError as error:
            print(
                f'image not found. error: {error} /\n imagem nao foi encontrada')

        lb_name = QLabel('username:', self)
        lb_name.move(20, 144)

        self.le_name = QLineEdit(self)
        self.le_name.resize(250, 24)
        self.le_name.move(90, 140)

        self.lb_full_name = QLabel('full name:', self)
        self.lb_full_name.move(20, 174)

        self.le_full_name = QLineEdit(self)
        self.le_full_name.resize(250, 24)
        self.le_full_name.move(90, 170)

        lb_new_password = QLabel('password:', self)
        lb_new_password.move(20, 204)

        self.le_new_password = QLineEdit(self)
        self.le_new_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.le_new_password.resize(250, 24)
        self.le_new_password.move(90, 200)

        lb_confirm = QLabel('confirm:', self)
        lb_confirm.move(20, 234)

        self.le_confirm = QLineEdit(self)
        self.le_confirm.setEchoMode(QLineEdit.EchoMode.Password)
        self.le_confirm.resize(250, 24)
        self.le_confirm.move(90, 230)
