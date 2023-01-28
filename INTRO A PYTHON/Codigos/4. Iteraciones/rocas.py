ini = int(input("Rocas iniciales? "))
pila = ini
t = 1

continuar = True
while continuar:

    
    print("Turno Jugador",t)

    preguntar = True
    while preguntar:

        print("Rocas en la pila:",pila)
        s = int(input("Rocas a sacar? "))
        if (s < 1) or (s > 5) or (s > pila):
            print("Invalido. Volver a intentar")
        else:
            preguntar = False
            pila = pila - s

    if pila == 0:
        continuar = False
    else:
        if t == 1:
            t = 2
        else:
            t = 1

print("Ganaste Jugador",t)
print("FINAL")
              
    


