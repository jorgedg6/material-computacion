import random

def num_abiertas(cs,x):
    num = 0
    a = x
    encontrado = False

    while not encontrado:
        v = cs[a]
        num += 1
        if v == x:
            encontrado = True
        else:
            a = v

    return num

def crear_cajas():

    ordenadas = []
    for i in range(0,100):
        ordenadas.append(i)

    desordenadas = []
    for i in range(0,100):
        x = random.randint(0,len(ordenadas)-1)
        a = ordenadas.pop(x)
        desordenadas.append(a)

    return desordenadas


#CODIGO PRINCIPAL
numlibres = 0
nummuertos = 0

#Numero de carceles donde jugar al juego
carceles = 10000
for c in range(0,carceles):
    
    #Crear cajas al azar
    cs = crear_cajas()

    #Cada prisionero se pone a abrir las cajas
    libres = True
    for i in range(0,100):
        if num_abiertas(cs,i) > 50:
            libres = False

    if libres:
        numlibres += 1
    else:
        nummuertos += 1

#Imprimir resultados
print("Veces LIBRES:",numlibres)
print("Veces MUERTOS:", nummuertos)




