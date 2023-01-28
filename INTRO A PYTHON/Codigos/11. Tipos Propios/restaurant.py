class Mesa:
    def __init__(self):
        self.ocupantes = 0
        self.cuenta = 0
        self.platos = []

    def ocupar_mesa(self, num_ocupantes):
        self.ocupantes = num_ocupantes

    def esta_vacia(self):
        return self.ocupantes == 0

    def agregar_plato(self, plato, precio):
        self.cuenta += precio
        self.platos.append(plato)

    def obtener_cuenta(self):
        return self.cuenta

    '''Obligado usar obtener_cuenta()'''
    def obtener_cuenta_por_persona(self):
        return self.obtener_cuenta() / self.ocupantes

    def obtener_platos(self):
        return self.platos

    def vaciar_mesa(self):
        self.ocupantes = 0
        self.cuenta = 0
        self.platos = []


class Restaurante:
    
    def __init__(self, nombre, num_mesas):
        self.nombre = nombre
        self.mesas = []
        for i in range(0,num_mesas):
            self.mesas.append(Mesa())

    def llegan_clientes(self, num_comensales):
        ix = -1
        for i in range(0,len(self.mesas)):
            mesa = self.mesas[i]
            if ix == -1 and mesa.esta_vacia():
                ix = i
                mesa.ocupar_mesa(num_comensales)
        return ix



#CODIGO PRINCIPAL (DCChurrasco )
r = Restaurante("DCChurrasco", 2)

continuar = True
while continuar:
    op = int(input("1-Llegan clientes 2-Pedir comida 3-La cuenta 9-Salir: "))

    if op == 1:
        num = int(input("Numero de clientes: "))
        ix = r.llegan_clientes(num)
        if ix == -1:
            print("No hay mesas disponibles :(")
        else:
            print("Sientense en la mesa", ix)

    elif op == 2:
        nm = int(input("Numero de mesa: "))
        plato = input("Plato: ")
        precio = int(input("Precio: "))
        r.mesas[nm].agregar_plato(plato, precio)

    elif op == 3:
        nm = int(input("Numero de mesa: "))
        mesa = r.mesas[nm]
        print("Pidieron", len(mesa.obtener_platos()), "platos")
        print("La cuenta son", mesa.obtener_cuenta())
        print("Eso hace", mesa.obtener_cuenta_por_persona(), "por persona")
        mesa.vaciar_mesa()

    elif op == 9:
        continuar = False
        print("Saliendo")





        
        

