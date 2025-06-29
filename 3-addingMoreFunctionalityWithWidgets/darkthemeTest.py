import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt6.QtWidgets import QPushButton

from PyQt6.QtCore import Qt
from PyQt6 import QtCore

import qdarktheme as qdark

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('CadastroCliente')

        self.lb_titulo = QLabel('Cadastrar Cliente', self)
        self.lb_titulo.move(10, 10)

        # campo nome
        self.lb_nome = QLabel('Nome:', self)
        self.le_nome = QLineEdit(self)

        self.lb_nome.move(50, 50)
        self.le_nome.move(100, 50)
        
        # campo sobrenome
        self.lb_sobrenome = QLabel('Sobrenome:', self)
        self.le_sobrenome = QLineEdit(self)
        
        self.lb_sobrenome.move(10, 100)
        self.le_sobrenome.move(100, 100)

        # campo idade
        self.lb_idade = QLabel('idade:', self)
        self.le_idade = QLineEdit(self)

        self.lb_idade.move(50, 150)
        self.le_idade.move(100, 150)
        # campo 
        self.lb_cpf = QLabel('CPF:', self)
        self.le_cpf = QLineEdit(self)

        self.lb_cpf.move(60, 200)
        self.le_cpf.move(100, 200)
        
        # campo de botões
        self.bt_limpar = QPushButton('Limpar Tudo', self)
        self.bt_limpar.clicked.connect(self.on_limpar)

        self.bt_cadastrar = QPushButton('Cadastrar', self)
        self.bt_cadastrar.setFixedWidth(200)
        self.bt_cadastrar.clicked.connect(self.on_cadastrar)

        self.bt_limpar.move(20, 250)
        self.bt_cadastrar.move(170, 250)
        
        # defaut test
        self.le_nome.insert('Fernando')
        self.le_sobrenome.insert('Fernandes')
        self.le_idade.insert('18')
        self.le_cpf.insert('12345678910')

    def on_limpar(self):
        self.le_nome.clear()
        self.le_sobrenome.clear()
        self.le_idade.clear()
        self.le_cpf.clear()
        
    def on_cadastrar(self):
        print('cadastro:')
        print('nome:', self.le_nome.text())
        print('sobrenome:', self.le_sobrenome.text())
        print('idade:', self.le_idade.text())
        print('CPF:', self.le_cpf.text())

        print('------------------------------------')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyleSheet(qdark.load_stylesheet())
        
    window = MainWindow()
    window.setGeometry(100, 100, 500, 500)
    window.show()
    sys.exit(app.exec())
