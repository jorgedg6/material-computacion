# Recibe una lista de votos,
# donde cada voto es una lista [str,str,int]
# con el nombre del pais que ha votado,
# a quien ha votado y cuantos puntos,
# y retorna un str con el ganador de Eurovision

def eurovision(vs):
    # Voy a crear una lista de listas [pais,puntos]
    # donde voy a ir sumando los puntos que vaya sacando
    # cada pais
    puntos = []

    #Para cada voto
    for v in vs:

        #Solo me interesa el pais que recibe los puntos y los puntos
        pais = v[1]
        pts = v[2]

        #Voy a buscar si ya tengo ese pais en mi lista de puntos
        #Y si lo tengo, le aumento los puntos
        esta = False
        for p in puntos:
            if p[0] == pais:
                esta = True
                p[1] += pts

        #Si no esta, me toca crearlo y ponerle los puntos
        if not esta:
            x = [pais,pts]
            puntos.append(x)

    #Aqui tendre en puntos todos los paises que han recibido puntos
    # y los puntos que tienen. Solo tengo que buscar quien tiene mas
    maxip = -1
    maxin = ""
    for p in puntos:
        if p[1] > maxip:
            maxip = p[1]
            maxin = p[0]

    return maxin



#CODIGO PRINCIPAL (TEST)

votos = [["Spain","Italy",10],
         ["Spain","Ireland",12],
         ["France","Ireland",8],
         ["France","Spain",1],
         ["Italy","Spain",10],
         ["Italy","Ireland",12]]

r = eurovision(votos)
print(r)
