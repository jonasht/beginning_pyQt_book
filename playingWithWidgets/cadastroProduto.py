import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QTextEdit
from util import *

AF_RIGHT = Qt.AlignmentFlag.AlignRight
AF_VCENTER = Qt.AlignmentFlag.AlignVCenter

class Cadastro_produto(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout = QVBoxLayout()

        layout_titulo = QHBoxLayout()
        layout_middle = QHBoxLayout()
        layout_middle2 = QVBoxLayout()
        layout_left = QVBoxLayout()
        layout_right = QVBoxLayout()

        layout_bts = QHBoxLayout()

        self.lb_titulo = QLabel('Cadastro de produto')
        layout_titulo.addWidget(self.lb_titulo)
        
        self.lb_produto = QLabel('Produto:', self)
        self.lb_produto.setAlignment(AF_RIGHT | AF_VCENTER)
        self.le_produto = QLineEdit(self)

        layout_left.addWidget(self.lb_produto)
        layout_right.addWidget(self.le_produto)

        self.lb_codigo = QLabel('Codigo:', self)
        self.lb_codigo.setAlignment(AF_RIGHT | AF_VCENTER)
        self.le_codigo = QLineEdit(self)
        

        layout_left.addWidget(self.lb_codigo)
        layout_right.addWidget(self.le_codigo)

        self.lb_preco = QLabel('R$:', self)
        self.lb_preco.setAlignment(AF_RIGHT | AF_VCENTER)
        self.le_preco = QLineEdit(self)

        layout_left.addWidget(self.lb_preco)
        layout_right.addWidget(self.le_preco)

        layout_middle.addLayout(layout_left)
        layout_middle.addLayout(layout_right)

        self.lb_descricao = QLabel('Descrição:', self)
        self.lb_descricao.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tt_descricao = QTextEdit(self)
        layout_middle2.addWidget(self.lb_descricao)
        layout_middle2.addWidget(self.tt_descricao)

        
        self.bt_limpar = QPushButton('Limpar', self)
        self.bt_cadastrar = QPushButton('Cadastrar')
        self.bt_limpar.setObjectName(DANGER)
        self.bt_cadastrar.setObjectName(SUCCESS)

        layout_bts.addWidget(self.bt_limpar)
        layout_bts.addWidget(self.bt_cadastrar)

        # add layouts no layout principal
        layout.addLayout(layout_titulo)
        layout.addLayout(layout_middle)
        layout.addLayout(layout_middle2)
        layout.addStretch()
        layout.addLayout(layout_bts)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Cadastro_produto()

    # colocando style theme
    with open('./style.css', 'r') as file:
        app.setStyleSheet(file.read())

    w.setGeometry(100, 100, 500, 500)
    w.show()
    sys.exit(app.exec())
