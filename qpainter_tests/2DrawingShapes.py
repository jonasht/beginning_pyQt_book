import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPainter, QColor

class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setPen(QColor(0, 0, 0))

        # Draw Line
        painter.drawLine(50, 50, 200, 50)

        # Draw Rectangle
        painter.setBrush(QColor(255, 0, 0))
        painter.drawRect(50, 100, 150, 100)

        # Draw Ellipse
        painter.setBrush(QColor(0, 0, 255))
        painter.drawEllipse(250, 100, 150, 100)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drawing Shapes with QPainter")
        self.setGeometry(100, 100, 400, 300)

        self.drawing_widget = DrawingWidget()
        self.setCentralWidget(self.drawing_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())