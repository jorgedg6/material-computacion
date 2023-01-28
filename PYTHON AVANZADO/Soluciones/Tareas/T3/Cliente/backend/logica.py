"""
Ventana principal del cliente que se encarga de funcionar como backend de la
mayoria de ventanas, de conectar señales y de procesar los mensajes recibidos
por el cliente
"""
from PyQt5.QtCore import pyqtSignal, QObject

from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_espera import VentanaEspera
from frontend.ventana_juego import VentanaJuego


class Logica(QObject):
    # Señales


    def __init__(self, parent):
        super().__init__()
        self.ventana_inicio = VentanaInicio()
        self.ventana_espera = VentanaEspera()
        self.ventana_juego = VentanaJuego()
        # -----------------------------------------
        self.descarga_actual = bytearray()
        self.parent = parent

        #  ==========> CONEXIONES <==========
        self.ventana_inicio.senal_envio_login.connect(
            parent.enviar
        )
        self.parent.senal_confirmacion_login.connect(
            self.ventana_inicio.ocultar_ventana
        )
        self.parent.senal_confirmacion_login.connect(
            self.ventana_espera.mostrar_ventana
        )
        self.parent.senal_denegacion_login.connect(
            self.ventana_inicio.error
        )
        self.parent.senal_actualizar_usuarios.connect(
            self.ventana_espera.actualizar_usuarios
        )
        self.ventana_espera.senal_comenzar_juego.connect(
            self.ventana_juego.mostrar_ventana
        )
    
    def manejar_mensaje(self, mensaje):
        comando = mensaje['comando']
