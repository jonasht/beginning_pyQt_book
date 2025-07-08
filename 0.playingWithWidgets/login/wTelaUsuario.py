from PyQt6.QtWidgets import (QApplication, QWidget, 
                            QVBoxLayout, QHBoxLayout, 
                            QLabel, QLineEdit, QTextEdit,
                            QPushButton, QFrame)
from PyQt6.QtCore import Qt
import sys
import util as u


class WTelaInicial(QWidget):
    def __init__(self, user_id=None) -> None:
        super().__init__()
        self.user_id = user_id
        self.state_btEditar = True

        
        layout_main = QVBoxLayout()
        layout_titulo = QVBoxLayout()
        layout_saudacao = QHBoxLayout()
        layout_texto = QVBoxLayout()
        layout_btsTexto = QHBoxLayout()
        layout_bts = QVBoxLayout()
        
        # titulo
        self.fr_titulo = QFrame()
        self.fr_titulo.setFixedWidth(140)
        self.fr_titulo.setFixedHeight(50)
        layout_fr_titulo = QVBoxLayout(self.fr_titulo)  # Layout para o frame
        self.lb_titulo = QLabel('User')
        layout_fr_titulo.addWidget(self.lb_titulo, alignment=Qt.AlignmentFlag.AlignCenter)

        layout_titulo.addWidget(self.fr_titulo, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.lb_titulo.setObjectName(u.INVERSE_INFO)
        self.fr_titulo.setObjectName(u.INFO)
        self.fr_titulo.setStyleSheet(u.TopTitle.lb)
        self.fr_titulo.setStyleSheet(u.TopTitle.fr)
        
        # layout nome boa vindas
        self.lb_saudacao = QLabel('bem vindo')
        self.lb_nome = QLabel('Humano')
        layout_saudacao.addWidget(self.lb_saudacao)
        layout_saudacao.addWidget(self.lb_nome)

        # texto 
        self.lb_mensagem = QLabel('Mensagem:')
        self.te_mensagem = QTextEdit()
        self.te_mensagem.setReadOnly(True)
        layout_texto.addWidget(self.lb_mensagem)
        layout_texto.addWidget(self.te_mensagem)
        # texto botoes
        self.bt_apagar = QPushButton('Apagar Tudo')
        self.bt_editar = QPushButton('Editar')
        self.bt_editar.clicked.connect(self.on_editar)
        
        layout_btsTexto.addWidget(self.bt_apagar)
        layout_btsTexto.addWidget(self.bt_editar)
        self.bt_apagar.setObjectName(u.DANGER)
        self.bt_editar.setObjectName(u.PRIMARY)
        layout_texto.addLayout(layout_btsTexto)

        # botoes
        self.bt_deslogar = QPushButton('Deslogar')
        self.bt_fechar = QPushButton('Fechar')
        layout_bts.addWidget(self.bt_deslogar)
        layout_bts.addWidget(self.bt_fechar)
        self.bt_deslogar.setObjectName(u.WARNING)
        self.bt_fechar.setObjectName(u.DANGER)
        
        layout_main.addLayout(layout_titulo)
        layout_main.addSpacing(10)
        layout_main.addLayout(layout_saudacao)
        layout_main.addLayout(layout_texto)
        
        layout_main.addSpacing(110)
        
        layout_main.addLayout(layout_bts)

        self.setLayout(layout_main)

    def on_editar(self):
        print('entrou no editar')
        if self.state_btEditar:
            self.bt_editar.setText('Salvar')
            self.bt_editar.setObjectName(u.SUCCESS)
            self.bt_editar.style().polish(self.bt_editar)
            self.te_mensagem.setReadOnly(False)
            self.te_mensagem.setFocus()
            
            
            self.state_btEditar = False
        else:
            self.bt_editar.setText('Editar')
            self.bt_editar.setObjectName(u.PRIMARY)
            self.bt_editar.style().polish(self.bt_editar)
            self.te_mensagem.setReadOnly(True)
            
            
            self.state_btEditar = True



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = WTelaInicial()
    widget.setStyleSheet(u.get_style())
    widget.setGeometry(100, 100, 1200, 900)
    widget.show()
    sys.exit(app.exec())