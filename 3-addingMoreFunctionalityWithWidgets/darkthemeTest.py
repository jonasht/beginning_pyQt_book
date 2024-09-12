import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# import theme
import qdarktheme



app = QApplication(sys.argv)
# apply the complete dar theme to qt app
qdarktheme.setup_theme('auto')

main_win = QMainWindow()
bt = QPushButton('dark theme')
main_win.setCentralWidget(bt)

main_win.show()

app.exec()