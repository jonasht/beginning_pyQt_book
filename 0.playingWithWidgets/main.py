from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication



class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        widget_left = Widget_left()
        widget_right = Widget_right()

        layout_main = QHBoxLayout()
        layout_main.addWidget(widget_left)
        layout_main.addWidget(widget_right)

        widget_main = QWidget()
        widget_main.setLayout(layout_main)

        self.setCentralWidget(widget_main)

        self.setup()
        
    def setup(self):
        
        self.show()
class Widget_right(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        
        self.lb = QLabel('bem vindo')
        layout.addWidget(self.lb)
        self.lb_nome = QLabel('Humano')
        layout.addWidget(self.lb_nome)

        self.setLayout(layout)
class Widget_left (QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout = QVBoxLayout()

        self.bt_home = QPushButton('Inicio')
        layout.addWidget(self.bt_home)

        self.bt_cadastrarProduto = QPushButton('Cadastrar Produto')
        layout.addWidget(self.bt_cadastrarProduto)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open('./styleV2.css', 'r') as file:
        app.setStyleSheet(file.read())

    
    window = MainWindow()
    window.setGeometry(100,100,500,400)

    
    window.show()
    sys.exit(app.exec())
    
    