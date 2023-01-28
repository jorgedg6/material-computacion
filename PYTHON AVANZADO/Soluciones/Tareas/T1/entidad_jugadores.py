from abc import ABC, abstractmethod
from parametros import BONIFICACION_TACANO, MULTIPLICADOR_BONIFICACION_BEBEDOR, \
                        PORCENTAJE_APUESTA_TACANO, BONIFICACION_SUERTE_CASUAL

class Jugador(ABC):
    
    def __init__(self, nombre, personalidad, energia,
                suerte, dinero, frustracion, ego,
                carisma, confianza, juego_favorito):
        self.nombre = nombre #str
        self.personalidad = personalidad #str
        self._energia = None #int 0-100
        self._suerte = None #int 0-50
        self._dinero = None #int > 0
        self._frustracion = None #int 0-100
        self._ego = None #int 0-15
        self._carisma = None #int 0-50
        self._confianza = None #int 0-30
        self.juego_favorito = juego_favorito #str

        #Seteo de parametros
        self.energia = energia
        self.suerte = suerte
        self.dinero = dinero
        self.frustracion = frustracion
        self.ego = ego
        self.carisma = carisma
        self.confianza = confianza

        self.juegos_jugados = [] #list Juego()
        pass

    @property
    def energia(self):
        return self._energia
    
    @energia.setter
    def energia(self, value):
        if 0 < value < 100:
            self._energia = value
        elif value < 0:
            self._energia = 0
        else:
            self._energia = 100
        pass

    @property
    def suerte(self):
        return self._suerte
    
    @suerte.setter
    def suerte(self, value):
        if 0 < value < 50:
            self._suerte = value
        elif value < 0:
            self._suerte = 0
        else:
            self._suerte = 50

    @property
    def dinero(self):
        return self._dinero
    
    @dinero.setter
    def dinero(self, value):
        if 0 < value:
            self._dinero = round(value)
        else:
            self._dinero = 0

    @property
    def frustracion(self):
        return self._frustracion
    
    @frustracion.setter
    def frustracion(self, value):
        if 0 < value < 100:
            self._frustracion = value
        elif value < 0:
            self._frustracion = 0
        else:
            self._frustracion = 100

    @property
    def ego(self):
        return self._ego
    
    @ego.setter
    def ego(self, value):
        if 0 < value < 15:
            self._ego = value
        elif value < 0:
            self._ego = 0
        else:
            self._ego = 15

    @property
    def carisma(self):
        return self._carisma
    
    @carisma.setter
    def carisma(self, value):
        if 0 < value < 50:
            self._carisma = value
        elif value < 0:
            self._carisma = 0
        else:
            self._carisma = 50
    
    @property
    def confianza(self):
        return self._confianza
    
    @confianza.setter
    def confianza(self, value):
        if 0 < value < 30:
            self._confianza = value
        elif value < 0:
            self._confianza = 0
        else:
            self._confianza = 30

    def comprar_bebestible(self, casino):
        casino.ver_bebestibles(casino)
        pass
    
    @abstractmethod
    def apostar(self, casino, apuesta, juego):
        porcentaje = apuesta / self.dinero * 100
        self.dinero -= apuesta
        self.energia -= round((self.ego + self.frustracion) * 0.15)

        #Definimos Favorito
        if juego.nombre == self.juego_favorito:
            favorito = 1
        else:
            favorito = 0
        
        prob = min(1,max(0,(self.suerte * 15 - apuesta * 0.4 + 
                            self.confianza * 3 * favorito
                            + self.carisma * 2) / 1000))
        
        resultado = juego.entregar_resultados(casino, apuesta, prob, favorito)

        if resultado:
            self.dinero += 2 * apuesta
            print("\n¡Enhorabuena! Has ganado",
                f"\nTu saldo actual es {self.dinero}")
            casino.evento_especial()
            return True, porcentaje
        else:
            print("\n¡Que mal! Has perdido",
                f"\nTu saldo actual es {self.dinero}")
            casino.evento_especial()
            return False, porcentaje
        

class Ludopata(Jugador):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass
    
    def apostar(self, casino, apuesta, juego):
        resultado_apuesta = super().apostar(casino, apuesta, juego)
        self._ludopatia(resultado_apuesta)
        pass

    def _ludopatia(self, apuesta):
        if not apuesta[0]:
            self.frustracion += 5
        self.ego += 2
        self.suerte += 3
        pass

class Tacano(Jugador):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

    def apostar(self, casino, apuesta, juego):
        resultado_apuesta = super().apostar(casino, apuesta, juego)
        self._tacano_extremo(resultado_apuesta)

    def _tacano_extremo(self, apuesta):
        if apuesta[0] and apuesta[1] < PORCENTAJE_APUESTA_TACANO:
            self.dinero += BONIFICACION_TACANO
            print("\n¡Has ganado una bonificación por tacaño!",
                f"\nTu saldo actual es {self.dinero}"
                )
        pass

class Bebedor(Jugador):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass
    
    def apostar(self, casino, apuesta, juego):
        super().apostar(casino, apuesta, juego)
        pass

    def cliente_recurrente(self):
        return MULTIPLICADOR_BONIFICACION_BEBEDOR

class Casual(Jugador):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

    def apostar(self, casino, apuesta, juego):
        super().apostar(casino, apuesta, juego)
        self._suerte_principiante(juego)
        pass
    
    def _suerte_principiante(self, juego):
        if juego in self.juegos_jugados:
            self.suerte += BONIFICACION_SUERTE_CASUAL
        pass