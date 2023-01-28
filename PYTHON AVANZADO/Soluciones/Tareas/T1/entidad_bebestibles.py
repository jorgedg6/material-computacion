from abc import ABC, abstractmethod
from random import randint
from parametros import MIN_ENERGIA_BEBESTIBLE, MAX_ENERGIA_BEBESTIBLE

class Bebestible(ABC):

    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.multiplicador = 1
    
    @abstractmethod
    def consumir(self, jugador):
        delta = randint(MIN_ENERGIA_BEBESTIBLE, MAX_ENERGIA_BEBESTIBLE)
        if jugador.personalidad == "Bebedor":
            self.multiplicador = jugador.cliente_recurrente()
        else:
            self.multiplicador = 1
        jugador.energia += delta * self.multiplicador
        print(f"\n¡Tu energía aumentó en {delta * self.multiplicador}!")
        pass

class Jugo(Bebestible):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def consumir(self, jugador):
        super().consumir(jugador)
        largo = len(self.nombre)
        if largo <= 4:
            jugador.ego += 4 * self.multiplicador
            print(f"\n¡Tu ego aumentó en {4 * self.multiplicador}!")
        elif 5 <= largo <= 7:
            jugador.suerte += 7 * self.multiplicador
            print(f"\n¡Tu suerte aumentó en {7 * self.multiplicador}!")
        elif 8 <= largo:
            jugador.frustracion -= 10 * self.multiplicador
            jugador.ego += 11 * self.multiplicador
            print(f"\n¡Tu frustración disminuyó en {10 * self.multiplicador}!")
            print(f"\n¡Tu ego aumentó en {11 * self.multiplicador}!")
        pass

class Gaseosa(Bebestible):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def consumir(self, jugador):
        super().consumir(jugador)
        if jugador.personalidad == 'Ludopata' or jugador.personalidad == 'Tacano':
            jugador.frustracion -= 5
            print(f"\n¡Tu frustración disminuyó en 5!")
        elif jugador.personalidad == 'Bebedor' or jugador.personalidad == 'Casual':
            jugador.frustracion += 5 * self.multiplicador
            print(f"\n¡Tu frustración aumentó en {5 * self.multiplicador}!")
        jugador.ego += 6 * self.multiplicador
        print(f"\n¡Tu ego aumentó en {6 * self.multiplicador}!")
        pass

class BrebajeMagico(Jugo, Gaseosa):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass
    
    def consumir(self, jugador):
        super().consumir(jugador)
        jugador.carisma += 5 * self.multiplicador
        print(f"\n¡Tu carisma aumentó en {5 * self.multiplicador}!")
        pass