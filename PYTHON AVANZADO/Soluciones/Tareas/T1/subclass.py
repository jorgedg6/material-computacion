from entidad_bebestibles import BrebajeMagico, Gaseosa, Jugo
from entidad_jugadores import Ludopata, Tacano, Bebedor, Casual
from entidad_juegos import Juego
from lectura import leer

def subclass_jugador():
    jugadores = leer("jugadores.csv")
    obj_jugador = []
    for jugador in jugadores:
        if jugador['personalidad'] == 'Ludopata':
            obj_jugador.append(Ludopata(**jugador))
        elif jugador['personalidad'] == 'Bebedor':
            obj_jugador.append(Bebedor(**jugador))
        elif jugador['personalidad'] == 'Tacano':
            obj_jugador.append(Tacano(**jugador))
        elif jugador['personalidad'] == 'Casual':
            obj_jugador.append(Casual(**jugador))
    
    return obj_jugador

def subclass_bebestible():
    bebestibles = leer("bebestibles.csv")
    obj_bebestible = []
    for bebestible in bebestibles:
        if bebestible['tipo'] == 'Jugo':
            obj_bebestible.append(Jugo(**bebestible))
        elif bebestible['tipo'] == 'Gaseosa':
            obj_bebestible.append(Gaseosa(**bebestible))
        elif bebestible['tipo'] == 'Brebaje mágico':
            obj_bebestible.append(BrebajeMagico(**bebestible))
    
    return obj_bebestible

def class_juego():
    juegos = leer("juegos.csv")
    obj_juego = []
    for juego in juegos:
        obj_juego.append(Juego(**juego))
    return obj_juego