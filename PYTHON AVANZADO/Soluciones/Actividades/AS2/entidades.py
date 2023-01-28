from abc import ABC, abstractmethod
from random import randint
from threading import Thread, Lock, Event, Timer
from time import sleep


class Persona(ABC, Thread):

    # Completar
    lock_bodega = Lock()
    lock_cola_pedidos = Lock()
    lock_cola_pedidos_listos = Lock()

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.disponible = True
        self.trabajando = True
        self.daemon = True

    @abstractmethod
    def run(self):
        pass


class Cocinero(Persona):

    def __init__(self, nombre, cocina):
        super().__init__(nombre)
        self.lugar_trabajo = cocina
        # Completar
        self.evento_plato_asignado = Event()

    def run(self):
        # Completar
        while self.trabajando:
            self.evento_plato_asignado.wait()
            sleep(randint(1,3))
            self.cocinar()
        pass

    def cocinar(self):
        # Completar
        self.disponible = False
        plato = self.sacar_plato()
        print(f'El cocinero {self.nombre} ha comenzado a cocinar {plato[1]}')
        self.buscar_ingredientes(plato, self.lugar_trabajo.bodega, self.lugar_trabajo.recetas)
        sleep(randint(1,3))
        self.agregar_plato(plato)
        self.evento_plato_asignado.clear()
        self.disponible = True
        pass

    def sacar_plato(self):
        # Completar
        with self.lock_cola_pedidos:
            plato = self.lugar_trabajo.cola_pedidos.popleft()
            return plato
        pass

    def buscar_ingredientes(self, plato, bodega, recetas):
        # Formato de los dicts entregados:
        # bodega = {
        #     "alimento_1": int cantidad_alimento_1,
        #     "alimento_2": int cantidad_alimento_2,
        # }
        # recetas = {
        #     "nombre_plato_1": [("ingrediente_1", "cantidad_ingrediente_1"),
        #                        ("ingrediente_2", "cantidad_ingrediente_2")],
        #     "nombre_plato_2": [("ingrediente_1", "cantidad_ingrediente_1"), 
        #                        ("ingrediente_2", "cantidad_ingrediente_2")]
        # }

        # Completar
        print(f'El cocinero {self.nombre} esta buscando ingredientes para {plato[1]}')
        with self.lock_bodega:
            ingredientes = recetas[plato[1]]
            for ingrediente in ingredientes:
                nombre = ingrediente[0]
                cantidad = ingrediente[1]
                bodega[nombre] -= int(cantidad)
            print(f'El cocinero {self.nombre} ha encontrado ingredientes para {plato[1]}')
        pass

    def agregar_plato(self, plato):
        # Completar
        with self.lock_cola_pedidos_listos:
            self.lugar_trabajo.cola_pedidos_listos.append(plato)
        pass


class Mesero(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)
        # Completar
        self.evento_manejar_pedido = Event()

    def run(self):
        # Completar
        while self.trabajando:
            if self.disponible:
                self.evento_manejar_pedido.set()
        pass

    def agregar_pedido(self, pedido, cocina):
        # Completar
        self.evento_manejar_pedido.clear()
        sleep(randint(1,2))
        with self.lock_cola_pedidos:
            cocina.cola_pedidos.append(pedido)
        self.evento_manejar_pedido.set()
        pass

    def entregar_pedido(self, cocina):
        # Completar
        with self.lock_cola_pedidos_listos:
            pedido = cocina.cola_pedidos_listos.popleft()
            print(f'El mesero {self.nombre} está entregando {pedido[1]} a la mesa {pedido[0]}')
            self.evento_manejar_pedido.clear()
            sleep(randint(1,3))
            self.pedido_entregado(pedido)
        pass

    def pedido_entregado(self, pedido):
        # Completar
        print(f'El pedido {pedido[1]} de la mesa {pedido[0]} fue entregado')
        self.evento_manejar_pedido.set()
        pass
