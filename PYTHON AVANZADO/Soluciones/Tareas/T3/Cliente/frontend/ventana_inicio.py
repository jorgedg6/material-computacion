import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QTimer, Qt
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QApplication
from os.path import join
from utils import data_json

window_name, base_class = uic.loadUiType(join(*data_json(
    "RUTA_VENTANA_INICIO")))


class VentanaInicio(window_name, base_class):
    # Señales
    senal_envio_login = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        '''
        Actualiza interfáz gráfica
        '''
        #Seteo del tamaño
        self.setFixedSize(640, 480)
        #Pixmap Logo
        pixmap_logo = QPixmap(join(*data_json('RUTA_LOGO')))
        self.label_logo.setPixmap(pixmap_logo)
        self.label_logo.setScaledContents(True)
        #Pixmap Fondo
        pixmap_fondo = QPixmap(join(*data_json('RUTA_FONDO')))
        self.label_fondo.setPixmap(pixmap_fondo)
        self.label_fondo.setScaledContents(True)
        #Texto Placeholder
        self.texto.setPlaceholderText('Ingresa tu nombre')
        #Conexion Boton
        self.boton.clicked.connect(self.enviar_login)
        #Mostrar Ventana
        self.mostrar_ventana()
    
    def enviar_login(self):
        self.senal_envio_login.emit({'nombre': self.texto.text(), 'comando': 'chequeo_login'})
        pass

    def error(self):
        self.texto.clear()
        self.texto.setPlaceholderText('Nombre inválido, iténtelo otra vez')

    def mostrar_ventana(self):
        self.show()
    
    def ocultar_ventana(self):
        self.hide()