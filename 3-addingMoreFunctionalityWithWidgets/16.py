
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
        
    def setUpWindow(self):
        self.login_is_successful = False
        
        lb_login = QLabel('login', self)
        lb_login.setFont(QFont('Arial', 20))
        lb_login.move(160, 10)

        lb_username = QLabel('username:')
        lb_username.move(20, 54)

        self.le_username = QLineEdit(self)
        self.le_username.resize(250, 24)
        self.le_username.move(90, 50)

        lb_password = QLabel('password:', self)
        lb_password.move(20, 86)

        self.le_password = QLineEdit(self)
        self.le_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.le_password.resize(250, 24)
        self.le_password.move(90, 82)
        
        # continuar ...

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    
    sys.exit(app.exec())
    