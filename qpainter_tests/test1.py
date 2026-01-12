import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit
)
from PyQt6.QtGui import QPainter, QColor
from style import *


class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event): #type: ignore
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.fillRect(self.rect(), QColor("white"))
        painter.setPen(QColor(0, 0, 0))
        painter.setBrush(QColor(255, 0, 0))
        painter.drawRect(50, 50, 100, 100)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()
        
        layout = QVBoxLayout()
        layout_container = QVBoxLayout()
        frame_container = QFrame()
        frame_container.setLayout(layout_container)
        
        self.lb_title = QLabel('teste numero 1, painter')
        layout_container.addWidget(self.lb_title)

        

        self.drawing_widget = DrawingWidget()
        
        layout_container.addWidget(self.drawing_widget)
        
        layout_bts = QHBoxLayout()
        bt_1 = QPushButton('botao')
        bt_2 = QPushButton('botao 2')
        layout_bts.addWidget(bt_1)
        layout_bts.addWidget(bt_2)
        bt_1.setObjectName(SUCCESS)
        bt_2.setObjectName(PRIMARY)


        layout_container.addLayout(layout_bts)

        layout.addWidget(frame_container)
        self.setLayout(layout)
        
    def initWindow(self):
        self.setWindowTitle('test 1')
        self.setGeometry(800, 800, 800, 500)
        self.setStyleSheet(get_style())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())