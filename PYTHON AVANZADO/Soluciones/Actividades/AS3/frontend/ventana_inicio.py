from email.charset import QP
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt5.QtGui import QPixmap

import parametros as p

class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()

        # Geometría
        self.setGeometry(600, 200, 500, 500)
        self.setWindowTitle('Ventana de Inicio')
        self.setStyleSheet("background-color: lightblue;")
        self.crear_elementos()

    def crear_elementos(self):
        # CCOMPLETAR
        self.setGeometry(200, 200, 500, 500)
        
        self.logo = QLabel(self)
        self.logo.setMaximumSize(400, 400)
        pixmap = QPixmap(p.RUTA_LOGO)
        self.logo.setPixmap(pixmap)
        self.logo.setScaledContents(True)

        h_usuario = QHBoxLayout()
        self.usuario_text = QLabel('Ingrese su usuario: ', self)
        self.usuario_form = QLineEdit('', self)
        h_usuario.addWidget(self.usuario_text)
        h_usuario.addWidget(self.usuario_form)

        h_clave = QHBoxLayout()
        self.clave_text = QLabel('Ingrese su contraseña: ', self)
        self.clave_form = QLineEdit('', self)
        self.clave_form.setEchoMode(QLineEdit.Password)
        h_clave.addWidget(self.clave_text)
        h_clave.addWidget(self.clave_form)

        self.boton = QPushButton('&Empezar Juego!', self)
        self.boton.clicked.connect(self.enviar_login)

        layout = QVBoxLayout()
        layout.addWidget(self.logo)
        layout.addLayout(h_usuario)
        layout.addLayout(h_clave)
        layout.addWidget(self.boton)
        
        self.setLayout(layout)
        pass

    def enviar_login(self):
        # COMPLETAR
        usuario = self.usuario_form.text()
        clave = self.clave_form.text()
        self.senal_enviar_login.emit((usuario, clave))
        pass

    def recibir_validacion(self, valid, errores):
        # COMPLETAR
        if valid:
            self.hide()
        if 'Usuario' in errores:
            self.usuario_form.setText('')
            self.usuario_form.setPlaceholderText('Usuario Inválido')
        if 'Contraseña' in errores:
            self.clave_form.setText('')
            self.clave_form.setPlaceholderText('Contraseña Inválida')
        pass


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaInicio()
    ventana.crear_elementos()
    ventana.show()
    sys.exit(app.exec_())
