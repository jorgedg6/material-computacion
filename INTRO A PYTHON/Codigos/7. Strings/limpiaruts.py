def limpiar_rut(sucio):
    #Nuevo string (oro) agregando solo los numeros o k o K
    oro = ""
    for c in sucio:
        if c in "0123456789":
            oro += c
        elif c in "kK":
            oro += "K"

    #Poner el oro en el formato correcto
    s = oro[:2]+"."+oro[2:5]+"."+oro[5:8]+"-"+oro[8:]
    return s


#CODIGO PRINCIPAL
print("EMPIEZA!")
continuar = True
while continuar:
    sucio = input("RUT: ")
    if sucio == "salir":
        continuar = False
    else:
        limpio = limpiar_rut(sucio)
        print("LIMPIO:", limpio)
print("FIN!")




