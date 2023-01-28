from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, QTimer
import parametros as p
from PyQt5 import uic
from random import randint
import sys

window_name, base_class = uic.loadUiType(p.RUTA_UI_POST_JUEGO)

class VentanaPostJuego(window_name, base_class):

    senal_escritura = pyqtSignal(tuple)
    senal_continuar = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(480, 640)
        self.boton_salir.clicked.connect(self.enviar_senal_escritura)
        self.boton_siguiente.clicked.connect(self.enviar_senal_continuar)
    
    def init_gui(self):
        self.label_nivel.setText(f'{self.nivel}')
        self.label_balas.setText(f'{self.balas} balas')
        self.label_tiempo.setText(f'{self.tiempo} seg')
        self.label_puntaje_total.setText(f'{self.puntaje_total} ptos')
        self.label_puntaje_nivel.setText(f'{self.puntaje_nivel} ptos')

        if self.status and self.nivel != 3:
            self.boton_siguiente.setEnabled(True)
            self.label_status.setText('Has dominado el nivel')
            self.label_status.setStyleSheet('background-color: green')
        else:
            self.boton_siguiente.setEnabled(False)
            self.label_status.setText('No has dominado el nivel')
            self.label_status.setStyleSheet('background-color: red')
        pass

    def mostrar_ventana(self, diccionario):
        self.nivel = diccionario['nivel']
        self.balas = diccionario['balas']
        self.tiempo = round(diccionario['tiempo'])
        self.puntaje_total = diccionario['puntaje_t']
        self.puntaje_nivel = diccionario['puntaje_n']
        self.usuario = diccionario['usuario']
        self.status = diccionario['status']

        self.init_gui()

        self.show()

    def enviar_senal_escritura(self):
        self.senal_escritura.emit((self.usuario, self.puntaje_total))
        self.cerrar_ventana()
        pass

    def enviar_senal_continuar(self):
        self.senal_continuar.emit(self.nivel + 1)
        pass

    def cerrar_ventana(self):
        self.hide()
    pass