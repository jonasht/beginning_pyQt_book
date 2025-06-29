# code for clearText() and accepttext() slots




import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

from PyQt6.QtCore import Qt
from PyQt6 import QtCore 

from theme import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 550, 250)
        self.setMaximumSize(510, 230)
        self.setWindowTitle('QlineEdit')
        
        self.setStyleSheet('''
                           QLineEdit{
                               border: 1px solid darkgrey;
                               border-radius: 2px;
                           }
                           QLineEdit:focus {
                               border: 1px solid lightgreen;
                           }
                           
                           ''')
        

        self.lb_titulo = QLabel('fazer cadastro',self)
        self.lb_titulo.move(10, 10)
        
        self.lb_nome = QLabel('nome:', self)
        self.lb_nome.move(20, 50)

        self.le_nome = QLineEdit(self)
        self.le_nome.resize(210, 20)
        self.le_nome.move(70, 50)

        self.lb_sobrenome = QLabel('sobrenome:', self)
        self.lb_sobrenome.move(20, 80)
        
        self.le_sobrenome = QLineEdit(self)
        self.le_sobrenome.resize(210, 20)
        self.le_sobrenome.move(70, 80)
        
        self.lb_idade = QLabel('idade:', self)
        self.lb_idade.move(20, 110)

        self.le_idade = QLineEdit(self)
        self.le_idade.resize(210, 20)
        self.le_idade.move(70, 110)
        
        
        
        self.clear_bt = QPushButton('clear', self)
        self.clear_bt.setStyleSheet('background-color: darkred; color:white;')
        self.clear_bt.move(140, 150)
        self.clear_bt.clicked.connect(self.clearText)

        self.bt_cadastrar = QPushButton('accept', self)
        self.bt_cadastrar.setStyleSheet('background-color:darkgreen; color:white;')
        self.bt_cadastrar.move(210, 150)
        self.bt_cadastrar.clicked.connect(self.cadastrar)
        
    def clearText(self):
        self.le_nome.clear()

    def cadastrar(self):
        print('nome:', self.le_nome.text())
        print('sobrenome:', self.le_sobrenome.text())
        print('idade:', self.le_idade.text())
        # self.close()
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            print('saindo da aplicacao')
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    