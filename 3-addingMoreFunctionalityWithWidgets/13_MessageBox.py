# second part of the code for the searchauthors() slot
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

    def searchAuthors(self):
        file = 'files/authors.txt'
        
        try:
            with  open(file, 'r') as f:
                authors = [line.rstrip('\n') for line in f]
            if self.le_author.txt() in authors:
                QMessageBox.information(self, 'author found', 'author found in catalogue', QMessageBox.standardButton.Ok)
            else:
                answer = QMessageBox.question(self, 'author not found',
                                          '''
                                          <p> do you wish to continue? </p>
                                          ''', QMessageBox.standardButton.Yes,
                                          QMessageBox.standardButton.No,
                                          QMessageBox.standardButton.No)

            if answer == QMessageBox.standardButton.No:
                print('closing application/fechando aplicacacao')
                self.close()


        except FileNotFoundError as error:
            QMessageBox.warning(self, 'error', f"""<p>file not found</p>
                                <p>Error {error}</p>
                                closing application""")
        
            self.close()


        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

    