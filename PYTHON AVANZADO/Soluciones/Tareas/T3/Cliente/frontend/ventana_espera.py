import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QTimer, Qt
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QApplication
from os.path import join
from utils import data_json
from random import choice

window_name, base_class = uic.loadUiType(join(*data_json(
    "RUTA_VENTANA_ESPERA")))

class VentanaEspera(window_name, base_class):
    # Señales
    senal_comenzar_juego = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.label_usuarios = {
            1: self.cliente_1,
            2: self.cliente_2,
            3: self.cliente_3,
            4: self.cliente_4,
        }
        for i in range(1,5):
            self.label_usuarios[i].setVisible(False)
        self.boton.setEnabled(False)
        self.admin = False

    def init_gui(self):
        '''
        Actualiza interfáz gráfica
        '''
        #Seteo del tamaño
        self.setFixedSize(640, 480)
        #Pixmap Fondo
        pixmap_fondo = QPixmap(join(*data_json('RUTA_FONDO')))
        self.label_fondo.setPixmap(pixmap_fondo)
        self.label_fondo.setScaledContents(True)

        self.boton.clicked.connect(self.comenzar_juego)
    
    def actualizar_usuarios(self, tupla):
        i = 1
        for usuario, color in tupla[0]:
            self.label_usuarios[i].setVisible(True)
            self.label_usuarios[i].setText(f'  {usuario}    {self.trans_color(color)}')
            i += 1
        if tupla[1]:
            self.admin = True
        if self.admin and i >= data_json('MINIMO_JUGADORES') + 1:
            self.boton.setEnabled(True)
        if i == data_json('MAXIMO_JUGADORES') + 1:
            self.comenzar_juego()
        pass

    def trans_color(self, color):
        if color == 'R':
            return 'Rojo'
        elif color == 'G':
            return 'Verde'
        elif color == 'B':
            return 'Azul'
        elif color == 'Y':
            return 'Amarillo'

    def comenzar_juego(self):
        self.ocultar_ventana()
        self.senal_comenzar_juego.emit()

    def mostrar_ventana(self):
        self.show()
    
    def ocultar_ventana(self):
        self.hide()