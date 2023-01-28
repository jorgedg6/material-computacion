import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QTimer, Qt
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QApplication
from os.path import join
from utils import data_json
from random import choice, randint

window_name, base_class = uic.loadUiType(join(*data_json(
    "RUTA_VENTANA_JUEGO")))

class VentanaJuego(window_name, base_class):
    # Señales


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_dobles = {
            'R': [self.label_doble_rojo, QPixmap(join(*data_json('RUTA_DOBLES_ROJO')))],
            'G': [self.label_doble_verde, QPixmap(join(*data_json('RUTA_DOBLES_VERDE')))],
            'B': [self.label_doble_azul, QPixmap(join(*data_json('RUTA_DOBLES_AZUL')))],
            'Y': [self.label_doble_amarillo, QPixmap(join(*data_json('RUTA_DOBLES_AMARILLO')))]
        }
        self.init_gui()

    def init_gui(self):
        '''
        Actualiza interfáz gráfica
        '''
        #Seteo del tamaño
        self.setFixedSize(640, 480)
        #Pixmap Tablero
        pixmap_tablero = QPixmap(join(*data_json('RUTA_TABLERO')))
        self.label_tablero.setPixmap(pixmap_tablero)
        self.label_tablero.setScaledContents(True)
        #Pixmap Dado
        pixmap_dado = QPixmap(join(*data_json('RUTA_DADO')))
        self.label_dado.setPixmap(pixmap_dado)
        self.label_dado.setScaledContents(True)

        for fichas in self.label_dobles.values():
            fichas[0].setPixmap(fichas[1])
            fichas[0].setScaledContents(True)
        
        self.boton.clicked.connect(self.dado)
    
    def dado(self):
        num = randint(0,6)
        self.texto_dado.setText(f'Numero Obtenido: {num}')
        return num

    def mostrar_ventana(self):
        self.show()
    
    def ocultar_ventana(self):
        self.hide()