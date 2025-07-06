from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
import sys
from PyQt6.QtCore import Qt
from util import *


class CadastroProduto(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout_main = QVBoxLayout()
        layout_titulo = QHBoxLayout()
        layout_meio = QHBoxLayout()
        layout_meio2 = QVBoxLayout()
        layout_left = QVBoxLayout()
        layout_right = QVBoxLayout()
        layout_bts = QHBoxLayout()


        # titulo 
        self.lb_titulo = QLabel('Cadastrar Produto')
        layout_titulo.addWidget(self.lb_titulo)
        
        # campo codigo
        self.lb_codigo = QLabel('Codigo:')
        self.le_codigo = QLineEdit()
        layout_left.addWidget(self.lb_codigo)
        layout_right.addWidget(self.le_codigo)
        
        # campo marca
        self.lb_marca = QLabel('Marca:')
        self.le_marca = QLineEdit()
        layout_left.addWidget(self.lb_marca)
        layout_right.addWidget(self.le_marca)
        
        # nome 
        self.lb_nome = QLabel('Nome:')
        self.le_nome = QLineEdit()
        layout_left.addWidget(self.lb_nome)
        layout_right.addWidget(self.le_nome)

        # campo preço
        self.lb_preco = QLabel('R$:')
        self.le_preco = QLineEdit()
        layout_left.addWidget(self.lb_preco)
        layout_right.addWidget(self.le_preco)

        # colocando layout left lbs e right les no meio
        layout_meio.addLayout(layout_left)
        layout_meio.addLayout(layout_right)
        
        # campo descrição
        self.lb_descricao = QLabel('Descrição')
        self.te_descricao = QTextEdit()
        
        layout_meio2.addWidget(self.lb_descricao)
        layout_meio2.addWidget(self.te_descricao)
        layout_meio2.addStretch()

        # campo botoes
        self.bt_limpar = QPushButton('Limpar')
        self.bt_cadastrar = QPushButton('Cadastrar')
        layout_bts.addWidget(self.bt_limpar)
        layout_bts.addWidget(self.bt_cadastrar)

        # add layouts main principais
        
        layout_main.addLayout(layout_titulo)
        layout_main.addLayout(layout_meio)
        layout_main.addLayout(layout_meio2)
        layout_main.addStretch()
        layout_main.addLayout(layout_bts)

        self.setLayout(layout_main)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(get_style())
    window = CadastroProduto()
    window.show()
    sys.exit(app.exec())
