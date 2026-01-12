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
        self.ceu_color = QColor('black')
        self.parede_color = QColor('darkblue')
        self.dentroDaCasa = QColor('gray')
        self.lampada_color = QColor('gray')
        self.noite_q = True
        
        

    def paintEvent(self, event): #type: ignore
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # ceu =============================================
        painter.fillRect(self.rect(), self.ceu_color)
        painter.setPen(QColor(0, 0, 0))

        # parede
        painter.setBrush(self.parede_color)
        painter.drawRect(300, 250, 500, 300)

        # porta
        painter.setBrush(QColor('brown'))
        painter.drawRect(445,435, 70, 115)
        
        painter.setBrush(self.lampada_color)
        painter.drawRect(450,440, 60, 200)
        
        # painter.drawRect(450,450, 50, 100)
        

        
        # telhado -==---------------------------------
        telhado = QPolygon([
        QPoint(550, 100), # Base direita
        QPoint(850, 250),   # Ponta direita
        QPoint(250, 250),  # Ponta 
        ])
        
        painter.setBrush(QColor('brown'))
        painter.drawPolygon(telhado)
        # definindo font -------------------
        # painter.setFont(QFont('Arial', 20))
        # text_var = 'esta eh uma casa'
        # painter.drawText(50, 150, text_var)
        
        # janela 
        painter.setBrush(QColor('brown'))
        painter.drawRect(645,396, 88, 78)
        
        painter.setBrush(self.lampada_color)
        painter.drawRect(650,400, 80, 70)

        painter.setBrush(QColor('brown'))
        painter.drawRect(685,400, 5, 70)
        
        painter.setBrush(QColor('brown'))
        painter.drawRect(650,435, 80, 5)

        
        # lua
        if self.noite_q:
            painter.setBrush(QColor('lightgray'))
            painter.drawEllipse(50, 50, 150, 150)
            painter.setBrush(QColor('gray'))
            painter.drawEllipse(100, 100, 10, 10)
            painter.drawEllipse(110, 160, 10, 10)
            painter.drawEllipse(130, 180, 20, 10)
        else:
        
        # sol -------------------------
            painter.setBrush(QColor('yellow'))
            painter.drawEllipse(950, 50, 150, 150)

            
        # grama
        painter.setBrush(QColor('green'))
        painter.drawRect(10, 550, 1240, 100)
        
        mato = QPolygon([
        QPoint(100, 500), # ponta
        QPoint(110, 600),   # Ponta direita
        QPoint(100, 600),  # Ponta esquerda
        ])
        painter.setBrush(QColor('darkgreen'))
        
        painter.drawPolygon(mato)
        
        #  teste ==-=-====================
        mato = QPolygon([
        QPoint(100+20, 500-10), # ponta
        QPoint(110+20, 600-10),   # Ponta direita
        QPoint(100+20, 600-10),  # Ponta esquerda
        ])
        painter.setBrush(QColor('darkgreen'))
        
        painter.drawPolygon(mato)
        
        mato = QPolygon([
        QPoint(100+30, 500-5), # ponta
        QPoint(110+30, 600-5),   # Ponta direita
        QPoint(100+30, 600-5),  # Ponta esquerda
        ])
        painter.setBrush(QColor('darkgreen'))
        
        painter.drawPolygon(mato)
        
        mato = QPolygon([
        QPoint(100+60, 500-5), # ponta
        QPoint(110+60, 600-5),   # Ponta direita
        QPoint(100+60, 600-5),  # Ponta esquerda
        ])
        painter.setBrush(QColor('darkgreen'))
        mato = QPolygon([
        QPoint(100+100, 500-5), # ponta
        QPoint(110+100, 600-5),   # Ponta direita
        QPoint(100+100, 600-5),  # Ponta esquerda
        ])
        painter.setBrush(QColor('darkgreen'))
        painter.drawPolygon(mato)

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
        self.bt_2 = QPushButton('Amanhecer')
        self.bt_close = QPushButton('Fechar')
        
        layout_bts.addWidget(self.bt_1)
        layout_bts.addWidget(self.bt_2)
        layout_bts.addWidget(self.bt_close)

        self.bt_1.setObjectName(SUCCESS)
        self.bt_2.setObjectName(SECONDARY)
        self.bt_close.setObjectName(DANGER)


        layout_container.addLayout(layout_bts)

        layout.addWidget(frame_container)
        self.setLayout(layout)
        
        # event bts
        self.bt_1.clicked.connect(self.set_lampada)
        self.bt_2.clicked.connect(self.set_tempo)
        self.bt_close.clicked.connect(lambda:self.close())
        
        

    def set_lampada(self):
        # Alterna a cor entre cinza (apagado) e amarelo (aceso)
        if self.drawing_widget.lampada_color == QColor('gray'):
            self.drawing_widget.lampada_color = QColor('yellow')
            self.bt_1.setText('Apagar')
            
        else:
            self.drawing_widget.lampada_color = QColor('gray')
            self.bt_1.setText('Acender')

        self.drawing_widget.update()
        
    def set_tempo(self):
        if self.drawing_widget.ceu_color == QColor('black'):
            self.drawing_widget.ceu_color = QColor('lightblue')
            self.drawing_widget.parede_color = QColor('blue')

            self.drawing_widget.noite_q = False
        else:
            self.drawing_widget.ceu_color=QColor('black')
            self.drawing_widget.parede_color = QColor('darkblue')
            self.drawing_widget.noite_q = True

        self.drawing_widget.update()


    def initWindow(self):
        self.setWindowTitle('qt qpainter ;)')
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