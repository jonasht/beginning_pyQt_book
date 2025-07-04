import sys
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QMainWindow
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import Qt
from util import *


class Main_window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.page_1 = Page_1()
        self.page_2 = Page_2()
        self.page_3 = Page_3()
        
        central_widget = QWidget()
        central_layout = QHBoxLayout()
        
        right_layout = QVBoxLayout()
        left_layout = QVBoxLayout()
        self.stack_widgets = QStackedWidget()
        self.stack_widgets.addWidget(self.page_1)
        self.stack_widgets.addWidget(self.page_2)
        self.stack_widgets.addWidget(self.page_3)

        self.bt_inicio = QPushButton('Inicio')
        self.bt_page2 = QPushButton('page 2')
        self.bt_page3 = QPushButton('page 3')
        left_layout.addWidget(self.bt_inicio)
        left_layout.addWidget(self.bt_page2)
        left_layout.addWidget(self.bt_page3)
        self.bt_inicio.setFixedWidth(200)

        self.bt_inicio.clicked.connect(lambda: self.stack_widgets.setCurrentIndex(0))
        self.bt_page2.clicked.connect(lambda: self.stack_widgets.setCurrentIndex(1))
        self.bt_page3.clicked.connect(lambda: self.stack_widgets.setCurrentIndex(2))

        right_layout.addWidget(self.stack_widgets)
        central_layout.addLayout(left_layout)
        central_layout.addLayout(right_layout)

        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)



    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            print('finalizando programa')
            self.close()
        
class Page_1(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QHBoxLayout()
        self.lb_bemvindo = QLabel('bem vindo')
        layout.addWidget(self.lb_bemvindo)
        self.setLayout(layout)  

class Page_2(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        self.lb = QLabel('22222222')
        self.lb1 = QLabel('está é a pagina 2')
        layout.addWidget(self.lb)
        layout.addWidget(self.lb1)
        self.setLayout(layout)  

class Page_3(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        self.lb1 = QLabel('33333333')
        self.le = QLineEdit()
        self.lb3 = QLabel('esta é a pagina 3')
        self.bt = QPushButton('botao 3')
        layout.addWidget(self.lb1)
        layout.addWidget(self.lb3)
        layout.addWidget(self.le)
        layout.addWidget(self.bt)
        self.setLayout(layout)  


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    main_window = Main_window()
    main_window.setGeometry(100, 100, 1000, 500)
    main_window.show()

    app.setStyleSheet(get_style())
    

    sys.exit(app.exec())