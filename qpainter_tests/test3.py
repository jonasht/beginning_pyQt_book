import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit
)
from PyQt6.QtGui import QKeyEvent, QPainter, QColor, QFont, QPolygon
from PyQt6.QtCore import Qt, QPoint
from style import *


class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.lampada_color = QColor('gray')

    def paintEvent(self, event): #type: ignore
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.fillRect(self.rect(), QColor("black"))
        painter.setPen(QColor(0, 0, 0))
        painter.setBrush(QColor('lightblue'))
        painter.drawRect(300, 250, 500, 300)

        # porta
        painter.setBrush(self.lampada_color)
        painter.drawRect(450,450, 50, 100)
        
        # telhado -==---------------------------------
        telhado = QPolygon([
        QPoint(550, 100), # Base direita
        QPoint(850, 250),   # Ponta direita
        QPoint(250, 250),  # Ponta 
        ])
        
        painter.setBrush(QColor('brown'))
        
        painter.drawPolygon(telhado)
        # definindo font
        
        
        painter.setFont(QFont('Arial', 20))
        text_var = 'esta eh uma casa'
        painter.drawText(50, 150, text_var)
        
        # janela 
        painter.setBrush(self.lampada_color)
        painter.drawRect(650,400, 80, 70)
        
        

        
    


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()
        
        layout = QVBoxLayout()
        layout_container = QVBoxLayout()
        frame_container = QFrame()
        frame_container.setLayout(layout_container)
        
        

        self.drawing_widget = DrawingWidget()
        
        layout_container.addWidget(self.drawing_widget)
        
        layout_bts = QVBoxLayout()
        self.bt_1 = QPushButton('Acender')
        bt_2 = QPushButton('Fechar')
        layout_bts.addWidget(self.bt_1)
        layout_bts.addWidget(bt_2)
        self.bt_1.setObjectName(SUCCESS)
        bt_2.setObjectName(DANGER)


        layout_container.addLayout(layout_bts)

        layout.addWidget(frame_container)
        self.setLayout(layout)
        
        # event bts
        self.bt_1.clicked.connect(self.set_lampada)
        bt_2.clicked.connect(lambda:self.close())

    def set_lampada(self):
        # Alterna a cor entre cinza (apagado) e amarelo (aceso)
        if self.drawing_widget.lampada_color == QColor('gray'):
            self.drawing_widget.lampada_color = QColor('yellow')
            self.bt_1.setText('Apagar')
            
        else:
            self.drawing_widget.lampada_color = QColor('gray')
            self.bt_1.setText('Acender')

        self.drawing_widget.update()


    def initWindow(self):
        self.setWindowTitle('test 1')
        self.setGeometry(800, 800, 1300, 800)
        self.setStyleSheet(get_style())
        
    def keyPressEvent(self, a0: QKeyEvent | None) -> None:
        if a0.key() == Qt.Key.Key_Escape: # type: ignore
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())