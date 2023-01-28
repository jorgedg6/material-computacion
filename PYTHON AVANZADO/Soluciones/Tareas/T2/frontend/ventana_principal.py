from PyQt5.QtWidgets import (
    QErrorMessage
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal
import parametros as p
from PyQt5 import uic

window_name, base_class = uic.loadUiType(p.RUTA_UI_PRINCIPAL)

class VentanaPrincipal(window_name, base_class):

    senal_volver = pyqtSignal()
    senal_enviar_usuario = pyqtSignal(tuple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        '''
        Inicializa los elementos de la interfáz gráfica
        '''
        self.setFixedSize(800, 500)
        
        pixmap = QPixmap(p.RUTA_FONDO_LUNA)
        self.foto_luna.setPixmap(pixmap)
        self.foto_luna.setScaledContents(True)

        pixmap = QPixmap(p.RUTA_ALIEN_LUNA)
        self.alien_luna.setPixmap(pixmap)
        self.alien_luna.setScaledContents(True)

        pixmap = QPixmap(p.RUTA_FONDO_JUPITER)
        self.foto_jupiter.setPixmap(pixmap)
        self.foto_jupiter.setScaledContents(True)
    
        pixmap = QPixmap(p.RUTA_ALIEN_JUPITER)
        self.alien_jupiter.setPixmap(pixmap)
        self.alien_jupiter.setScaledContents(True)
        
        pixmap = QPixmap(p.RUTA_FONDO_GALAXIA)
        self.foto_galaxia.setPixmap(pixmap)
        self.foto_galaxia.setScaledContents(True)
        
        pixmap = QPixmap(p.RUTA_ALIEN_GALAXIA)
        self.alien_galaxia.setPixmap(pixmap)
        self.alien_galaxia.setScaledContents(True)
        
        self.boton.clicked.connect(self.enviar_usuario)

    def enviar_usuario(self):
        if self.selector_luna.isChecked():
            self.senal_enviar_usuario.emit((self.user_form.text(), 1))
        elif self.selector_jupiter.isChecked():
            self.senal_enviar_usuario.emit((self.user_form.text(), 2))
        elif self.selector_galaxia.isChecked():
            self.senal_enviar_usuario.emit((self.user_form.text(), 3))

    def pop_error(self, error):
        '''
        Muestra el Error de nombre usuario
        '''
        msg = QErrorMessage(self)
        msg.setStyleSheet("background-color: #8ec9db")
        msg.showMessage(error)

    def closeEvent(self, event):
        '''
        Muestra la ventana de inicio y cierra la de ranking
        al cerrar la pestaña
        '''
        event.accept()
        self.senal_volver.emit()
        self.hide()

    def mostrar_ventana(self):
        '''
        Muestra la ventana principal
        '''
        self.show()
    
    def cerrar_ventana(self):
        '''
        Cierra la ventana principal
        '''
        self.hide()