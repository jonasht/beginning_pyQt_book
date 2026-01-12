import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPainter, QColor, QFont
from style import *


class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event): # type: ignore
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setPen(QColor(255, 255, 100))
        painter.setFont(QFont('Arial', 20))
        painter.drawText(50, 50, "oi, PyQt6!")
        painter.drawText(50, 100, "oi, PyQt6!")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(get_style())

        self.setWindowTitle("Drawing Text with QPainter")
        self.setStyleSheet(get_style())
        self.setGeometry(100, 100, 400, 300)
        

        self.drawing_widget = DrawingWidget()
        self.setCentralWidget(self.drawing_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())