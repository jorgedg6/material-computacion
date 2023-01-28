from lectura import escribir

class LogicaPostJuego:
    def __init__(self):
        pass
    
    def escribir(self, tupla):
        usuario, puntaje = tupla
        escribir(usuario, puntaje)