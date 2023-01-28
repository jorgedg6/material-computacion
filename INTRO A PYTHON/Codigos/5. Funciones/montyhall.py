import random

'''Funcion que juega una partida.
Parametro: un bool que dice cambiara de puerta.
Retorno: un bool diciendo si gana.'''
def jugar(cambia):
    #Colocar el auto
    auto = random.randint(0,2)

    #Colocar las cabras en las otras puertas
    if auto == 0:
        cabra1 = 1
        cabra2 = 2
    elif auto == 1:
        cabra1 = 0
        cabra2 = 2
    else:
        cabra1 = 0
        cabra2 = 1

    #El participante elige
    eleccion = random.randint(0,2)

    #Calcular cual es la puerta alternativa que queda despues
    #de abrir una cabra
    if (eleccion == cabra1) or (eleccion == cabra2):
        #Abres la otra cabra, y por tanto la alternativa es la puerta del auto
        alternativa = auto
    else:
        #Si elije el auto, abrimos la cabra1 por ejemplo, y solo queda cabra2
        alternativa = cabra2

    #Cambia su eleccion o no dependiendo del parametro
    if cambia:
        eleccion = alternativa

    #Miramos si ha ganado
    ganado = (eleccion == auto)

    #Devolvemos si ha ganado o no
    return ganado


#PROGRAMA PRINCIPAL
num_partidas = 100000

#Jugar sin cambiar
vsincambiar = 0
for i in range(0,num_partidas):
    ganado = jugar(False)
    if ganado:
        vsincambiar += 1

#Jugar cambiando
vcambiar = 0
for i in range(0, num_partidas):
    ganado = jugar(True)
    if ganado:
        vcambiar += 1

#Imprimir resultados
print("Victorias SIN CAMBIAR:",vsincambiar,"/",num_partidas)
print("Victorias CAMBIANDO:",vcambiar,"/", num_partidas)


    
    



