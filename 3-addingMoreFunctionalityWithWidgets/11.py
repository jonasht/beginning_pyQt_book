from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QLineEdit, QPushButton
import sys
from PyQt6.QtGui import QFont



class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 340, 140)
        self.setWindowTitle('messagebox')

        self.setUpMainWindow()
        self.show()
    def setUpMainWindow(self):
        catalogue_lb = QLabel('author catalogue/catalago de autor', self)
        catalogue_lb.move(100, 10)

        catalogue_lb.setFont(QFont('Arial', 18))

        lb_search = QLabel('search the index for an author:', self)
        lb_search.move(20, 40)

        lb_author = QLabel('name:', self)
        lb_author.move(20, 74)

        self.le_author = QLineEdit(self)
        self.le_author.move(70, 70)
        self.le_author.resize(240, 24)
        self.le_author.setPlaceholderText('enter name as: first & last')

        bt_search = QPushButton('search', self)
        bt_search.move(140, 100)
        bt_search.clicked.connect(self.searchAuthors)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

    