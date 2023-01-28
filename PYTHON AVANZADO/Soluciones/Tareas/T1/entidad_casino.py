from random import random, randint
from parametros import DEUDA_TOTAL, PROBABILIDAD_EVENTO, SHOW_ACTUAL, DINERO_SHOW
from subclass import subclass_bebestible, class_juego, subclass_jugador
from entidad_show import Show

class Casino:

    def __init__(self):
        self.jugadores = subclass_jugador()
        self.jugador = None
        self.bebestibles = subclass_bebestible()
        self.juegos = class_juego()
        self.dinero_faltante = DEUDA_TOTAL

        self.menu_inicio()
        pass
    
    def menu_inicio(self):
        print("\n" + " Menú Inicio ".center(30, "=") + "\n")
        print(
            "[1] Iniciar Partida\n" + 
            "[X] Salir\n"
            )
        input_usuario = input("Seleccione una opción: ")
        if input_usuario == "1":
            self.menu_jugadores()
        elif input_usuario == "X" or input_usuario == "x":
            print("\n¡Esperamos volver a verte pronto!\n")
            quit()
        else:
            print("\nPor favor introduzca una opción válida")
            self.menu_inicio()

    def menu_jugadores(self):
        print("\n" + " Menú Jugadores ".center(30, "=") + "\n")
        i = 1
        for jugador in self.jugadores:
            print(f"[{i}] {jugador.nombre}: {jugador.personalidad}")
            i += 1
        print(
            "[0] Volver\n" + 
            "[X] Salir\n"
            )
        input_usuario = input("Seleccione una opción: ")
        if input_usuario.isnumeric():
            if 0 < int(input_usuario) <= len(self.jugadores):
                jugador = self.jugadores[int(input_usuario)-1]
                self.jugador = jugador
                self.menu_principal()

            elif input_usuario == "0":
                self.menu_inicio()
            else:
                print("\n Por favor introduzca una opción válida")
                self.menu_jugadores()
        else:
            if input_usuario == "X" or input_usuario == "x":
                print("\n¡Esperamos volver a verte pronto!\n")
                quit()
            else:
                print("\n Por favor introduzca una opción válida")
                self.menu_jugadores()
        
    def menu_principal(self):
        if self.jugador.dinero >= self.dinero_faltante:
            print("\n** ¡Enhorabuena! Ya puedes pagar la deuda al casino **")
            print(
                "\n¿Que deseas hacer?\n", 
                "\n[0]Seguir Jugando",
                "\n[X]Pagar y salir"
            )
            input_usuario = input("\nSeleccione una opción: ")
            if input_usuario == "0":
                pass
            elif input_usuario == "X" or input_usuario == "x":
                print("\n¡Has ganado! Esperamos volver a verte\n")
                quit()
            else:
                print("\n Por favor introduzca una opción válida")
                self.menu_principal()
        
        print("\n" + " Menú Principal ".center(30, "=") + "\n")
        print(
            "[1] Opciones de Juegos\n" + 
            "[2] Comprar bebestible\n" + 
            "[3] Habilidades jugador\n" + 
            "[4] Ver Show\n" +
            "[0] Volver\n" + 
            "[X] Salir\n" +
            f"\nSaldo Actual: {self.jugador.dinero}"
            f"\nDinero Faltante: {max(0,self.dinero_faltante - self.jugador.dinero)}\n"
            )
        input_usuario = input("Seleccione una opción: ")

        if input_usuario == "1":
            self.ver_juegos()
        elif input_usuario == "2":
            self.ver_bebestibles()
        elif input_usuario == "3":
            self.habilidades_jugador()
        elif input_usuario == "4":
            print(f"\nDeseas ver el show \"{SHOW_ACTUAL}\" por ${DINERO_SHOW}")
            print(
            "\n[1] Confirmar\n" + 
            "[0] Volver\n"
            )
            input_usuario_show = input("Seleccione una opción: ")
            if input_usuario_show == "1":
                Show(self.jugador)
                self.menu_principal()
            elif input_usuario_show == "0":
                self.menu_principal()
            else:
                print("\n Por favor introduzca una opción válida")
                self.menu_principal()
        elif input_usuario == "0":
            self.menu_jugadores()
        elif input_usuario == "X" or input_usuario == "x":
            print("\n¡Esperamos volver a verte pronto!\n")
            quit()
        else:
            print("\n Por favor introduzca una opción válida")
            self.menu_principal()

    def evento_especial(self):
        if random() <= PROBABILIDAD_EVENTO:
            bebestible = self.bebestibles[randint(0,len(self.bebestibles)-1)]
            print(f"\n**¡Has ganado un bebestible gratis! {bebestible.nombre} **")
            bebestible.consumir(self.jugador)
    
    def jugar(self, juego):
        if juego.apuesta_minima > self.jugador.dinero:
            print("\nNo tienes dinero suficiente para apostar en este juego")
        else:
            print(f"\nPuede apostar entre {juego.apuesta_minima} y {juego.apuesta_maxima}")
            apuesta = input("\n¿Cuánto desea apostar?: ")
            if apuesta.isnumeric():
                if juego.apuesta_minima <= int(apuesta) <= juego.apuesta_maxima:
                    self.jugador.apostar(self, int(apuesta), juego)
                    self.jugador.juegos_jugados.append(juego)
                else:
                    print("\nNo puede apostar esa cantidad")
            else:
                print("\nIngrese una opción válida")
        pass

    def ver_juegos(self):
        print("\n" + " Opciones de Juegos ".center(30, "=") + "\n")
        i = 1
        for juego in self.juegos:
            print(f"[{i}] {juego.nombre}")
            i += 1
        print(
            "[0] Volver\n" + 
            "[X] Salir\n"
            )
        input_usuario = input("Seleccione una opción: ")
        if input_usuario.isnumeric():
            if 0 < int(input_usuario) <= len(self.juegos):
                juego = self.juegos[int(input_usuario)-1]
                self.jugar(juego)
                self.ver_juegos()
            elif input_usuario == "0":
                self.menu_principal()
            else:
                print("\n Por favor introduzca una opción válida")
                self.ver_juegos()
        else:
            if input_usuario == "X" or input_usuario == "x":
                print("\n¡Esperamos volver a verte pronto!\n")
                quit()
            else:
                print("\n Por favor introduzca una opción válida")
                self.ver_juegos()
    
    def habilidades_jugador(self):
        print("\n" + " Estado Jugador ".center(30, "=") + "\n")
        print(
            f"Nombre: {self.jugador.nombre}\n" + 
            f"Personalidad: {self.jugador.personalidad}\n" + 
            f"Energía: {self.jugador.energia}\n" + 
            f"Suerte: {self.jugador.suerte}\n" + 
            f"Dinero: {self.jugador.dinero}\n" + 
            f"Frustración: {self.jugador.frustracion}\n" + 
            f"Ego: {self.jugador.ego}\n" + 
            f"Carisma: {self.jugador.carisma}\n" + 
            f"Confianza: {self.jugador.confianza}\n" + 
            f"Juego Favorito: {self.jugador.juego_favorito}\n" + 
            f"Dinero Faltante: {max(0,self.dinero_faltante - self.jugador.dinero)}\n"
            )
        print(    
            "[0] Volver\n" + 
            "[X] Salir\n"
            )
        input_usuario = input("Seleccione una opción: ")

        if input_usuario == "0":
            self.menu_principal()
        elif input_usuario == "X" or input_usuario == "x":
            print("\n¡Esperamos volver a verte pronto!\n")
            quit()
        else:
            print("\nPor favor introduzca una opción válida")
            self.habilidades_jugador()
        
    def ver_bebestibles(self):
        print("\n" + " Bebestibles ".center(82, "=") + "\n")
        i = 1
        print("Nº".center(10, " "), "|", "Nombre".center(25, " "), "|",
                "Tipo".center(25, " "), "|", "Precio".center(20, " "))
        print("-" * 84)
        for bebestible in self.bebestibles:
            print(f"[{i}]".center(10, " "), "|", 
            bebestible.nombre.center(25, " "), "|", 
            bebestible.tipo.center(25, " "), "|", 
            ("$"+str(bebestible.precio)).center(20, " ")
            )
            i += 1
        print(
            "\n[0] Volver\n" + 
            "[X] Salir\n"
            )
        input_usuario = input("Seleccione una opción: ")

        if input_usuario.isnumeric():
            if 0 < int(input_usuario) <= len(self.bebestibles):
                bebestible = self.bebestibles[int(input_usuario) - 1]
                if bebestible.precio > self.jugador.dinero:
                    print("\nNo tienes suficiente dinero para comprar este producto")
                    self.ver_bebestibles()
                else:
                    self.jugador.dinero -= bebestible.precio
                    bebestible.consumir(self.jugador)
                    self.menu_principal()
            elif input_usuario == "0":
                self.menu_principal()
            else:
                print("\nSeleccione una opción válida")
                self.ver_bebestibles()
        else:
            if input_usuario == "X" or input_usuario == "x":
                print("\n¡Esperamos volver a verte pronto!\n")
                quit()
            else:
                print("\n Por favor introduzca una opción válida")
                self.ver_bebestibles()