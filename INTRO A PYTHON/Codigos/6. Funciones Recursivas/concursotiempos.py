
'''
def ftiempos(n):
    for i in range(0,n):
        print("Tiempo",i)
    print("SE ACABO")

#CODIGO PRINCIPAL
ftiempos(10)
'''


'''
def ftiempos(n):
    print("Tiempo",n)


#CODIGO PRINCIPAL
ftiempos(10)
'''



'''
def ftiempos(n):
    print("Tiempo", n)
    ftiempos(n)

#CODIGO PRINCIPAL
ftiempos(10)
'''


'''
def ftiempos(n):
    print("Tiempo", n)
    ftiempos(n+1)

#CODIGO PRINCIPAL
ftiempos(10)

'''

def ftiempos(i,n):
    print("Tiempo",i)
    ftiempos(i+1,n)

#CODIGO PRINCIPAL
ftiempos(0,10)



'''
def ftiempos(i,n):
    if i == n:
        print("SE ACABO")
    else:
        print("Tiempo",i)
        ftiempos(i+1,n)

#CODIGO PRINCIPAL
ftiempos(0,10)
'''

'''
def ftiempos(i,n):
    if i == n:
        print("SE ACABO")
    else:
        print("Tiempo",i)
        ftiempos(i+1,n)


#CODIGO PRINCIPAL
ftiempos(0,10)
'''

'''


#FUNCION RECURSIVA (se llama a si misma)
def miprint(i,n):

    #CASO BASE
    #El final, caso mas pequeno, cuando quieres acabar
    if i == n:
        print("SE ACABO")

    #CASO RECURSIVO
    #Incluye una llamada a si mismo, pero cada vez un paso mas alla
    #acercandose al final (caso base)
    else:
        print("Tiempo",i)
        miprint(i+1,n)

'''
