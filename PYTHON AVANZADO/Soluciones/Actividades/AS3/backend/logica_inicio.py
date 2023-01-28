from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, list)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, tupla_respuesta):
        # COMPLETAR
        errores = []
        validez = True
        if not tupla_respuesta[0].isalnum() or len(tupla_respuesta[0]) > p.MAX_CARACTERES:
            validez = False
            errores.append('Usuario')
        if tupla_respuesta[1] != p.PASSWORD:
            validez = False
            errores.append('Contraseña')
        
        self.senal_respuesta_validacion.emit(validez, errores)

        if validez:
            self.senal_abrir_juego.emit(tupla_respuesta[0])

        pass
