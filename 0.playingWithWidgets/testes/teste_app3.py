import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout

from PyQt6.QtCore import Qt

from util import *

import qdarktheme

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout_h = QHBoxLayout()
        layout_v1 = QVBoxLayout()
        layout_v2 = QVBoxLayout()


        self.setWindowTitle('cadastrarProduto')

        layout_titulo = QHBoxLayout()
        layout_titulo.addStretch()
        self.lb_titulo = QLabel('Cadastrar Produto')
        layout_titulo.addWidget(self.lb_titulo)
        layout_titulo.addStretch()

        
        self.lb_nome = QLabel('Nome:', self)
        self.lb_nome.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout_v1.addWidget(self.lb_nome)

        self.le_nome = QLineEdit(self)
        layout_v2.addWidget(self.le_nome)


        self.lb_preco = QLabel('R$:', self)
        self.lb_preco.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout_v1.addWidget(self.lb_preco)

        self.le_preco = QLineEdit(self)
        layout_v2.addWidget(self.le_preco)
        
        self.lb_qtd = QLabel('Quantidade:', self)
        layout_v1.addWidget(self.lb_qtd)

        self.le_qtd = QLineEdit(self)
        layout_v2.addWidget(self.le_qtd)




        layout_h.addLayout(layout_v1)
        layout_h.addLayout(layout_v2)

        layout_bts = QHBoxLayout()
        self.bt_limpar = QPushButton('Limpar')
        self.bt_limpar.setObjectName(DANGER)
        layout_bts.addWidget(self.bt_limpar)
        
        self.bt_cadastrar = QPushButton('Cadastrar', self)
        self.bt_cadastrar.setObjectName(SUCCESS)        
        layout_bts.addWidget(self.bt_cadastrar)
        
        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_titulo)
        layout_main.addLayout(layout_h)
        layout_main.addStretch()

        layout_main.addLayout(layout_bts)
        
        self.setLayout(layout_main)

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    
    with open('./Style.css', 'r') as f:
        qss = f.read()
        app.setStyleSheet(qss)

    
    window = MainWindow()
    window.setGeometry(100, 100, 500, 500)
    window.show()
    sys.exit(app.exec())