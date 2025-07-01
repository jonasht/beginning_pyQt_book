from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit
import sys
from util import *


class W_CadastroPessoa(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout_main = QVBoxLayout()
        layout_cima = QHBoxLayout()
        layout_meio = QHBoxLayout()
        layout_left = QVBoxLayout()
        layout_right = QVBoxLayout()
        layout_bts = QHBoxLayout()
        # titulo
        self.lb_titulo = QLabel('Cadastro Cliente')
        layout_cima.addStretch()
        layout_cima.addWidget(self.lb_titulo)
        layout_cima.addStretch()

        # nome
        self.lb_nome = QLabel('Nome:')
        self.le_nome = QLineEdit()
        layout_left.addWidget(self.lb_nome)
        layout_right.addWidget(self.le_nome)

        # cpf
        self.lb_cpf = QLabel('CPF:')
        self.le_cpf = QLineEdit()
        layout_left.addWidget(self.lb_cpf)
        layout_right.addWidget(self.le_cpf)
        # telefone
        self.lb_telefone = QLabel('Telefone:')
        self.le_telefone = QLineEdit()
        layout_left.addWidget(self.lb_telefone)
        layout_right.addWidget(self.le_telefone)

        # email 
        self.lb_email = QLabel('E-mail:')
        self.le_email = QLineEdit()
        layout_left.addWidget(self.lb_email)
        layout_right.addWidget(self.le_email)

        # botoes 
        self.bt_limpar = QPushButton('Limpar')
        self.bt_limpar.setObjectName(DANGER)
        self.bt_cadastrar = QPushButton('Cadastrar')
        self.bt_cadastrar.setObjectName(SUCCESS)
        
        layout_bts.addWidget(self.bt_limpar)
        layout_bts.addWidget(self.bt_cadastrar)
# 

        layout_meio.addLayout(layout_left)
        layout_meio.addLayout(layout_right)
        layout_main.addLayout(layout_cima)
        layout_main.addLayout(layout_meio)
        layout_main.addLayout(layout_bts)
        
        self.setLayout(layout_main)
if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyleSheet(get_style())

    widget = W_CadastroPessoa()
    widget.show()
    sys.exit(app.exec())
