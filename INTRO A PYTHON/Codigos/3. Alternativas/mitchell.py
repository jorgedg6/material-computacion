'''
Vas a hacer tu primer programa de Inteligencia Artificial
basado en el famoso libro 'Machine Learning' de Mitchell (pg. 53),
para ver si se puede o no jugar al tenis basado en las
condiciones metereológicas.

Input:
- Clima (int: 1-soleado, 2-lluvioso 3-nublado)
- Viento (str: "fuerte" o "debil")
- Humedad (float)

Si es nublado -> SI
Si llueve pero hay poco viento debil -> Si y si hay fuerte -> No
Si es soleado y la humedad es alta (mas o igual que 70) -> no si es baja -> Si

No preguntar las 3 cosas (puede cansar al usuario). Solo preguntar si es
necesario para decidir. 
'''

c = int(input("1-Soleado 2-Lluvioso 3-Nublado: "))

if c == 3:
    print("SI")

elif c == 1:
    h = int(input("Humedad: "))

    if h >= 70.0:
        print("NO")
    else:
        print("SI")
        
elif c == 2:
    v = input("Viento: ")

    if v == "fuerte":
        print("NO")
    else:
        print("SI")



