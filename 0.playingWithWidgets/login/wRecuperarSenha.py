from PyQt6.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QLabel, QPushButton, QLineEdit, QFrame
)
from PyQt6.QtCore import Qt
import sys
import util as u


class WRecuperarSenha(QWidget):
    def __init__(self) -> None:
        super().__init__()

        
        layout_main = QVBoxLayout()
        layout_cima = QHBoxLayout()
        layout_middle = QVBoxLayout() 
        layout_InMiddle = QGridLayout()
        layout_baixo = QGridLayout()

        
        # --- Bloco do Título com Frame ---
        self.frame_titulo = QFrame()
        self.frame_titulo.setObjectName(u.INFO) # Define o nome do objeto para o CSS
        self.frame_titulo.setStyleSheet(u.TopTitle.frame)
        self.frame_titulo.setFixedWidth(250)
        self.frame_titulo.setFixedHeight(50)
        
        # Layout para o frame, para poder centralizar o texto
        layout_fr_titulo = QVBoxLayout(self.frame_titulo)
        
        self.lb_titulo = QLabel('Recuperar Senha')
        self.lb_titulo.setObjectName(u.INVERSE_INFO)
        
        # Adiciona o label ao layout do frame, centralizando
        layout_fr_titulo.addWidget(self.lb_titulo, alignment=Qt.AlignmentFlag.AlignCenter)

        
        # Adiciona o frame (que já contém o título) ao layout de cima, centralizando
        layout_cima.addWidget(self.frame_titulo, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        # email
        self.lb_email = QLabel('Email:')
        self.le_email = QLineEdit()
        layout_InMiddle.addWidget(self.lb_email, 0, 0)
        layout_InMiddle.addWidget(self.le_email, 0, 1)

        # senha
        self.lb_senha = QLabel('Nova Senha:')
        self.le_senha = QLineEdit()
        self.lb_reSenha = QLabel('Repetir Senha:')
        self.le_reSenha = QLineEdit()

        # Adicionando os widgets de senha na grade, especificando linha e coluna
        layout_InMiddle.addWidget(self.lb_senha, 1, 0)
        layout_InMiddle.addWidget(self.le_senha, 1, 1)
        layout_InMiddle.addWidget(self.lb_reSenha, 2, 0)
        layout_InMiddle.addWidget(self.le_reSenha, 2, 1)
        
        # botoes
        self.bt_recuperar = QPushButton('Recuperar Senha')
        self.bt_redefinir = QPushButton('Redefinir Senha')
        self.lb_infoSenha = QLabel('senhadddddddd')
   
        self.bt_voltar = QPushButton('Voltar')

        layout_baixo.addWidget(self.bt_recuperar, 0, 0)
        layout_baixo.addWidget(self.bt_redefinir, 0, 1)
        layout_baixo.addWidget(self.lb_infoSenha, 1, 0)
        layout_baixo.addWidget(self.bt_voltar, 2, 0)

        layout_middle.addLayout(layout_InMiddle)

        layout_main.addLayout(layout_cima)
        layout_main.addSpacing(20) # Adiciona um espaço
        layout_main.addLayout(layout_middle)
        layout_main.addLayout(layout_baixo)
        self.setLayout(layout_main)

    # esc p sair
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WRecuperarSenha()
    window.setGeometry(100, 100, 1200, 900)
    window.show()
    app.setStyleSheet(u.get_style())
    

    sys.exit(app.exec())
        

        
