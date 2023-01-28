from collections import deque
from entidades import Cocinero, Mesero
from time import sleep
from random import randint


class Cocina:

    def __init__(self, bodega, recetas):
        super().__init__()
        self.cola_pedidos = deque()
        self.cola_pedidos_listos = deque()
        self.cocineros = []
        self.meseros = []
        self.bodega = bodega
        self.recetas = recetas
        self.abierta = True

    def initialize_threads(self):
        # Completar
        for cocinero in self.cocineros:
            Cocinero.start(cocinero)
        for mesero in self.meseros:
            Mesero.start(mesero)
        pass

    def asignar_cocinero(self):
        # Completar
        while self.abierta:
            sleep(1)
            if len(self.cola_pedidos)>0:
                cocinero = False
                i = 0
                while not cocinero:
                    cocinero = self.cocineros[i].disponible
                    if cocinero:
                        self.cocineros[i].evento_plato_asignado.set()
                    i += 1
                    if i >= len(self.cocineros):
                        i = 0
        pass

    def asignar_mesero(self):
        # Completar
        while self.abierta:
            sleep(1)
            if len(self.cola_pedidos_listos)>0:
                mesero = False
                i = 0
                while not mesero:
                    mesero = self.meseros[i].disponible
                    if mesero:
                        self.meseros[i].evento_manejar_pedido.set()
                        self.meseros[i].entregar_pedido(self)
                    i += 1
                    if i >= len(self.meseros):
                        i = 0
        self.finalizar_jornada_laboral()
        pass

    def finalizar_jornada_laboral(self):
        for mesero in self.meseros:
            mesero.trabajando = False

        for cocinero in self.cocineros:
            cocinero.trabajando = False
