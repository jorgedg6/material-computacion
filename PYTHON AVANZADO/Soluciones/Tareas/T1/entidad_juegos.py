from random import random
from parametros import EGO_GANAR, CARISMA_GANAR, FRUSTRACION_GANAR, \
                        FRUSTRACION_PERDER, CONFIANZA_PERDER

class Juego:

    def __init__(self, nombre, esperanza, apuesta_minima, apuesta_maxima):
        self.nombre = nombre
        self.esperanza = esperanza
        self.apuesta_minima = apuesta_minima
        self.apuesta_maxima = apuesta_maxima
        pass

    def entregar_resultados(self, casino, apuesta, prob_jugador, favorito):
        if random() <= self.probabilidad_de_ganar(apuesta, prob_jugador, favorito):
            casino.jugador.ego += EGO_GANAR
            casino.jugador.carisma += CARISMA_GANAR
            casino.jugador.frustracion -= FRUSTRACION_GANAR
            return True
        else:
            casino.jugador.frustracion += FRUSTRACION_PERDER
            casino.jugador.confianza -= CONFIANZA_PERDER
            return False

    def probabilidad_de_ganar(self, apuesta, prob_jugador, favorito):
        return min(1, prob_jugador - (apuesta - (favorito * 50 - (self.esperanza) * 30)) / 10000)