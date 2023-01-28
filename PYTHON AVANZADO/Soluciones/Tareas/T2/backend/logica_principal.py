from PyQt5.QtCore import QObject, pyqtSignal

class LogicaPrincipal(QObject):

    senal_iniciar = pyqtSignal(tuple)
    senal_error = pyqtSignal(str)
    senal_confirmacion = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def chequear_datos(self, tupla):
        '''
        Verifica la validez de el nombre de usuario
        y emite la señal para abrir el nivel seleccionado
        '''
        usuario, nivel = tupla
        if len(usuario) == 0:
            self.senal_error.emit('Nombre de usuario no puede ser vacio')
        elif not usuario.isalnum():
            self.senal_error.emit('Nombre de usuario sólo debe contener valores alfanuméricos')
        else:
            self.senal_confirmacion.emit()
            self.senal_iniciar.emit((usuario, nivel))