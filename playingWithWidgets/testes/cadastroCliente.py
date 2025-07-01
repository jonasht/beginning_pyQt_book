import sys

from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QApplication
from util import *

AlignRight = Qt.AlignmentFlag.AlignRight
AlignVCenter = Qt.AlignmentFlag.AlignVCenter

class Cadastro_Widget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout()

        lay_titulo = QHBoxLayout()
        lay_meio = QHBoxLayout()
        lay_left = QVBoxLayout()
        lay_right = QVBoxLayout()
        lay_bts = QHBoxLayout()

        
        self.lb_titulo = QLabel('Cadastrar Cliente', self)
        lay_titulo.addStretch()
        lay_titulo.addWidget(self.lb_titulo)
        lay_titulo.addStretch()

        self.lb_nome = QLabel('Nome:', self)
        self.lb_nome.setAlignment(AlignRight | AlignVCenter)
        self.le_nome = QLineEdit(self)
        lay_left.addWidget(self.lb_nome)
        lay_right.addWidget(self.le_nome)

        self.lb_cpf = QLabel('CPF:', self)
        self.lb_cpf.setAlignment(AlignRight | AlignVCenter)
        
        self.le_cpf = QLineEdit(self)
        
        lay_left.addWidget(self.lb_cpf)
        lay_right.addWidget(self.le_cpf)

        self.lb_fone = QLabel('Telefone:', self)
        self.lb_fone.setAlignment(AlignRight | AlignVCenter)
        self.le_fone = QLineEdit(self)
        

        lay_left.addWidget(self.lb_fone)
        lay_right.addWidget(self.le_fone)

        # botoes
        self.bt_limpar = QPushButton('Limpar')
        self.bt_limpar.setObjectName(DANGER)
        self.bt_cadastrar = QPushButton('Cadastrar', self)
        self.bt_cadastrar.setObjectName(SUCCESS)
        lay_bts.addWidget(self.bt_limpar)
        lay_bts.addWidget(self.bt_cadastrar)


        lay_meio.addLayout(lay_left)
        lay_meio.addLayout(lay_right)

        # layouts principais

        layout.addLayout(lay_titulo)

        layout.addLayout(lay_meio)
        layout.addStretch()
        layout.addLayout(lay_bts)
        
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    
    window = Cadastro_Widget()
    
    with open('./style.css', 'r') as file:
        app.setStyleSheet(file.read())

    window.setGeometry(100, 100, 500, 500)

    window.show()
    sys.exit(app.exec())

    
    

    