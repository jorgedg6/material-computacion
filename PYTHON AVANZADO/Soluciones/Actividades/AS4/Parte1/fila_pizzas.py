class Cliente:
    def __init__(self, nombre):
        # Completar
        self.nombre = nombre
        self.siguiente = None
        pass


    def __str__(self):
        # NO MODIFICAR
        return self.nombre

class FilaPizza:
    def __init__(self):
        # Completar
        self.primero = None
        self.ultimo = None
        self.largo = 0
        pass


    def llega_cliente(self, cliente: Cliente):
        # Completar
        if self.largo == 0:
            self.ultimo = cliente
            self.primero = cliente
        else:
            self.ultimo.siguiente = cliente
            self.ultimo = cliente
        self.largo += 1
        pass

    def alguien_se_cuela(self, cliente: Cliente, posicion: int):
        # Completar
        if self.largo == 0:
            self.ultimo = cliente
            self.primero = cliente
        elif posicion == 0:
            cliente.siguiente = self.primero
            self.primero = cliente
        elif posicion >= self.largo:
            self.ultimo.siguiente = cliente
            self.ultimo = cliente
        else:
            nodo_actual = self.primero
            for _ in range(posicion - 1):
                nodo_actual = nodo_actual.siguiente
            cliente.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente = cliente
        self.largo += 1
        pass
    
    def cliente_atendido(self):
        # Completar
        if self.largo <= 0:
            pass
        else:
            if self.largo == 1:
                atendido = self.primero
                self.primero = None
                self.ultimo = None
            else:
                atendido = self.primero
                self.primero = self.primero.siguiente
            self.largo -= 1
            return atendido


    def __str__(self):
        # Completar
        string = ''
        nodo_actual = self.primero
        while nodo_actual:
            string += f'{nodo_actual.nombre}, '
            nodo_actual = nodo_actual.siguiente
        return string[:-2]


if __name__ == "__main__":
    print("\nNO DEBES EJECUTAR AQUÍ EL PROGRAMA!!!!")
    print("Ejecuta el main.py\n")
    raise(ModuleNotFoundError)