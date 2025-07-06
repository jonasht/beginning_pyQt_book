import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
from util import *

class Widget_main(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout_main = QVBoxLayout()

        layout_lbs = QHBoxLayout()
        layout_les = QHBoxLayout()
        layout_bts = QHBoxLayout()

        self.bt_primary = QPushButton('primary', self)
        self.bt_secondary = QPushButton('secondary', self)
        self.bt_success = QPushButton('success', self)
        self.bt_warning = QPushButton('warning', self)
        self.bt_danger = QPushButton('danger', self)
        self.bt_info = QPushButton('info', self)
        
        self.bt_primary.setObjectName(PRIMARY)
        self.bt_secondary.setObjectName(SECONDARY)
        self.bt_success.setObjectName(SUCCESS)
        self.bt_warning.setObjectName(WARNING)
        self.bt_danger.setObjectName(DANGER)
        self.bt_info.setObjectName(INFO)

        
        
        layout_bts.addWidget(self.bt_primary)
        layout_bts.addWidget(self.bt_secondary)
        layout_bts.addWidget(self.bt_success)
        layout_bts.addWidget(self.bt_warning)
        layout_bts.addWidget(self.bt_danger)
        layout_bts.addWidget(self.bt_info)
        
        layout_main.addLayout(layout_bts)
        self.setLayout(layout_main)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open('./styleTest.css', 'r') as file:
        app.setStyleSheet(file.read())
    w = Widget_main()
    
    w.show()
    sys.exit(app.exec())