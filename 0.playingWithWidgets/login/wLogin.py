from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
import sys
import util as u


class Login(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout_main = QVBoxLayout()
        layout_title = QHBoxLayout()
        layout_campos = QHBoxLayout()
        layout_lbs = QVBoxLayout()
        layout_les = QVBoxLayout()
        layout_bts = QVBoxLayout()
        layout_link = QHBoxLayout()

        # titulo 
        layout_title.addStretch()
        self.lb_title = QLabel('login')

        layout_title.addWidget(self.lb_title)
        layout_title.addStretch()
        
        self.lb_title.setStyleSheet(u.Text.title)
        
        # login
        self.lb_login = QLabel('Login:')
        self.le_login = QLineEdit()

        layout_lbs.addWidget(self.lb_login)
        layout_les.addWidget(self.le_login)
        # senha
        self.lb_senha = QLabel('Senha:')
        self.le_senha = QLineEdit()
        layout_lbs.addWidget(self.lb_senha)
        layout_les.addWidget(self.le_senha)
        layout_campos.addStretch()
        layout_campos.addLayout(layout_lbs)
        layout_campos.addLayout(layout_les)
        layout_campos.addStretch()
        
        # botoes
        self.bt_login = QPushButton('Entrar')
        self.bt_login.setObjectName(u.SUCCESS)
        self.bt_cadastrar = QPushButton('Fazer Cadastro')
        self.bt_esqueceuSenha = QPushButton('esqueceu a senha?')
        self.bt_cadastrar.setObjectName(u.INFO)
        self.bt_esqueceuSenha.setObjectName(u.LINK)
        
        layout_bts.addWidget(self.bt_login)
        layout_bts.addWidget(self.bt_cadastrar)
        layout_link.addStretch()
        layout_link.addWidget(self.bt_esqueceuSenha)
        
        # self.bt_esqueceuSenha.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        # colocando layouts principais
        layout_main.addLayout(layout_title)
        layout_main.addStretch()
        layout_main.addLayout(layout_campos)
        layout_main.addStretch()

        
        layout_main.addLayout(layout_bts)
        layout_main.addLayout(layout_link)

        self.setLayout(layout_main)
        
        
    # esc p sair
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    widget = Login()
    widget.setGeometry(100, 100, 500, 500)
    app.setStyleSheet(u.get_style())
    # remover o bar 
    widget.setWindowFlag(Qt.WindowType.FramelessWindowHint)
    widget.show()
    sys.exit(app.exec())


    