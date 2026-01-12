import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit
)
from PyQt6.QtGui import QKeyEvent, QPainter, QColor, QFont, QPolygon
from PyQt6.QtCore import Qt, QPoint
from style import *
from random import randint

class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ceu_color = QColor('black')
        self.parede_color = QColor('darkblue')
        self.dentroDaCasa = QColor('gray')
        self.lampada_color = QColor('gray')
        self.noite_q = True
        
        # lista de numeros aleatorio
        self.numeros_ale = [randint(1, 15) for _ in range(30)]

        

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
        
        

        
        for i in self.numeros_ale:
            mato = QPolygon([
            QPoint(00+25*i, 90+450-30), # ponta
            QPoint( 2+25*i, 90+500-30),   # Ponta direita
            QPoint(00+25*i, 90+500-30),  # Ponta esquerda
            ])
            painter.setBrush(QColor('lightgreen'))
            painter.drawPolygon(mato)
        
        
            mato = QPolygon([
            QPoint(00+20*i+10, 100+450-30), # ponta
            QPoint( 2+20*i+10, 100+500-30),   # Ponta direita
            QPoint(00+20*i+10, 100+500-30),  # Ponta esquerda
            ])
            painter.setBrush(QColor('lightgreen'))
            painter.drawPolygon(mato)
        
            mato = QPolygon([
            QPoint(00+20*i+15, 110+450-30), # ponta
            QPoint( 2+20*i+15, 110+500-30),   # Ponta direita
            QPoint(00+20*i+15, 110+500-30),  # Ponta esquerda
            ])
            painter.setBrush(QColor('green'))
            painter.drawPolygon(mato)
            
            mato = QPolygon([
            QPoint(00+2+20*i+15, 110+450-30), # ponta
            QPoint( 2+  20*i+15, 110+505-30),   # Ponta direita
            QPoint(00+  20*i+15, 110+500-30),  # Ponta esquerda
            ])
            painter.setBrush(QColor('green'))
            painter.drawPolygon(mato)
            
            mato = QPolygon([
            QPoint(00+2+20*i+20, 110+450-30), # ponta
            QPoint( 2+  20*i+20, 110+505-30),   # Ponta direita
            QPoint(00+  20*i+20, 110+500-30),  # Ponta esquerda
            ])
            painter.setBrush(QColor('darkgreen'))
            painter.drawPolygon(mato)
            
            mato = QPolygon([
            QPoint(00+2+20*i+25, 110+450-30), # ponta
            QPoint( 2+  20*i+25, 110+505-30),   # Ponta direita
            QPoint(00+  20*i+25, 110+500-30),  # Ponta esquerda
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
            self.bt_2.setText('Anoitecer')
        else:
            self.drawing_widget.ceu_color=QColor('black')
            self.drawing_widget.parede_color = QColor('darkblue')
            self.drawing_widget.noite_q = True
            self.bt_2.setText('Amanhacer')

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