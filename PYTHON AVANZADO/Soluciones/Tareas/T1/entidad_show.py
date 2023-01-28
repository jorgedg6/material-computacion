from parametros import DINERO_SHOW, ENERGIA_SHOW, FRUSTRACION_SHOW

class Show:
    def __init__(self,jugador):
        self.jugador = jugador
        self._atributos_show()
        pass
    
    def _atributos_show(self):
        if self.jugador.dinero < DINERO_SHOW:
            print("\nNo tienes el dinero suficiente para pagar el show")
        else:
            self.jugador.dinero -= DINERO_SHOW
            print(f"\nTu saldo actual es {self.jugador.dinero}")
            self.jugador.energia += ENERGIA_SHOW
            print(f"\n¡Tu energía aumentó en {ENERGIA_SHOW}!")
            self.jugador.frustracion += FRUSTRACION_SHOW
            print(f"\n¡Tu frustración disminuyó en {FRUSTRACION_SHOW}!")
        pass
