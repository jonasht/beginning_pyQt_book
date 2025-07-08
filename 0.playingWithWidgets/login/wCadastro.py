from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit
import sys
import util as u 

class WCadastro(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout_main = QVBoxLayout()
        layout_title = QHBoxLayout()
        layout_lbs = QVBoxLayout()
        layout_les = QVBoxLayout()
        layout_middle = QHBoxLayout()
        layout_bts = QVBoxLayout()

        # titulo
        self.lb_titulo = QLabel('Fazer Cadastro')
        layout_title.addWidget(self.lb_titulo)
        
        # usuario
        self.lb_user = QLabel('Usuario:')
        self.le_user = QLineEdit()
        layout_lbs.addWidget(self.lb_user)
        layout_les.addWidget(self.le_user)

        # nome 
        self.lb_nome = QLabel('Nome:')
        self.le_nome = QLineEdit()
        layout_lbs.addWidget(self.lb_nome)
        layout_les.addWidget(self.le_nome)

        # sobrenome
        self.lb_sobrenome = QLabel('Sobrenome:')
        self.le_sobrenome = QLineEdit()
        layout_lbs.addWidget(self.lb_sobrenome)
        layout_les.addWidget(self.le_sobrenome)
        
        # email
        self.lb_email = QLabel('Email:')
        self.le_email = QLineEdit()

        # senha
        self.lb_senha = QLabel('Senha:')
        self.le_senha = QLineEdit()
        layout_lbs.addWidget(self.lb_senha)
        layout_les.addWidget(self.le_senha)
        
        # senha 2
        self.lb_senha2 = QLabel('repetir Senha:')
        self.le_senha2 = QLineEdit()
        layout_lbs.addWidget(self.lb_senha2)
        layout_les.addWidget(self.le_senha2)
        
        layout_middle.addLayout(layout_lbs)
        layout_middle.addLayout(layout_les)

        # botoes
        self.bt_cadastrar = QPushButton('Cadastrar')
        self.bt_resetar = QPushButton('Resetar')
        self.bt_voltar = QPushButton('Voltar')
        layout_bts.addWidget(self.bt_cadastrar)
        layout_bts.addWidget(self.bt_resetar)
        layout_bts.addWidget(self.bt_voltar)
        # add layouts 
        layout_main.addLayout(layout_title)
        layout_main.addStretch()
        layout_main.addLayout(layout_middle)
        layout_main.addLayout(layout_bts)
        
        self.setLayout(layout_main)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    widget = WCadastro()
    widget.setGeometry(100, 100, 500, 500)
    widget.setStyleSheet(u.get_style())

    widget.show()

    sys.exit(app.exec())
