def ubicar_h(C,P,I):
    
    palh = C[I][0]#Pal H actual
    posh = C[I][1]#Pos negrita en Pal H

    nv = palh[posh]#Letra negrita Pal V
    np = P[posh]#Letra negrita Pal dada

    buenlargo = (len(palh) == len(P))
    buennegrita = (nv == "" or nv == np)

    #Si correcto, actualizar
    if buenlargo and buennegrita:
        for i in range(0,len(P)):
            C[I][0][i] = P[i]

    return C
    


def ubicar_v(C,P):

    nlv = len(C) #Num letras verticales

    buenlargo = (len(P) == nlv)

    #Mirar las letras que hay en la negrita
    #Y mirar si coinciden con la parabra dada
    buennegrita = True
    for i in range(0,nlv):
        palh = C[i][0]#Pal H actual
        posh = C[i][1]#Pos negrita en Pal H
        nv = palh[posh]#Letra negrita Pal V
        np = P[i]#Letra negrita Pal dada

        #Si no es espacio y no coinciden
        if nv != "" and nv != np:
            buennegrita = False

    #Actualizar
    if buenlargo and buennegrita:
        for i in range(0,len(P)):
            posh = C[i][1]
            C[i][0][posh] = P[i]
        
    return C
    



C1 = [
        [["","","F",""],2],
        [["M","O","R","A","D","O"],3],
        [["","R"],1],
        [["","","O","",""],2]
    ]

uh = ubicar_h(C1,["F","L","O","J","O"],3)
print(uh)


C2 = [
        [["","","F",""],2],
        [["M","O","R","A","D","O"],3],
        [["","R"],1],
        [["","","O","",""],2]
    ]

uv = ubicar_v(C2,["C","A","R","O"])
print(uv)

C3 = [
        [["","","F",""],2],
        [["M","O","R","A","D","O"],3],
        [["","R"],1],
        [["","","O","",""],2]
    ]


