# Recibe una lista de estudiantes,
# donde cada estudiante es una lista [str,float]
# con el nombre y la nota, y retorna
# una lista de str con los nombres
# de los que tienen 1.1

def unouno(p):
    #Lista donde pondre los nombres que encuentre
    res = []
    
    #Recorrer estudiante a estudiante
    for e in p:
        # e es un esudiante ([str,float])
        # El nombre esta en la posicion 0, y la nota en la 1
        nombre = e[0]
        nota = e[1]
        # Si tiene 1.1 lo agrego a mi lista de nombre
        if nota == 1.1:
            res.append(nombre)

    #Retorno la lista de nombres
    return res
        


#CODIGO PRINCIPAL (TEST)

est = [["Alice",5.5],
       ["Bob",1.1],
       ["Charlie",6.8],
       ["David",1.1],
       ["Eva",7.0]]
        
r = unouno(est)
print(r)
