import sys 
from PyQt6.QtWidgets import QWidget, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout



class Window(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        