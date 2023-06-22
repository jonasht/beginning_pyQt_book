
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
        
        self.cb_showPassword = QCheckBox('show password', self)
        self.cb_showPassword.move(90, 110)

        self.cb_showPassword.toggled.connect(self.displayPasswordIfChecked)

        # 
        bt_login = QPushButton('login', self)
        bt_login.resize(320, 34)
        bt_login.move(20, 140)
        bt_login.clicked.connect(self.clickLoginButton)

        lb_not_member = QLabel('not a member?', self)
        lb_not_member.move(20, 186)

        bt_sign_up = QPushButton('sign up', self)
        bt_sign_up.move(120, 180)
        bt_sign_up.clicked.connect(self.createNewUser)
    
    def clickLoginButton(self):
        users = {}
        file = 'file/users.txt'

        try:
            with open(file, 'r') as reader:
                for line in reader:
                    user_info = line.split(' ')
                    username_info = user_info[0]
                    password_info = user_info[1].strip('\n')
                    users[username_info] = password_info
            
            username = self.le_username.text()
            password = self.le_password.text()

            if (username, password) in users.items():
                QMessageBox.information(self,
                                        'login successful',
                                        'login sucessful',
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok
                                        )
                self.login_is_successful =True
                self.close()
                self.openApplicationWindow()
            else:
                QMessageBox.warning(self, 'error message', 'the username or password is incorrect', 
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)

        except FileNotFoundError as error:
            QMessageBox.warning(self, 'error',
                                f'''<p> file not found </p>''',
                                f'''error: {error} ''',
                                QMessageBox.StandardButton.Ok
                                
                                )
            
            # create file if it doesnt exit/ criar file se ele nao existe
            f = open(file, 'w')
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    
    sys.exit(app.exec())
    