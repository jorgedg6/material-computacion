def sanitize(s):

    #Miro letra a letra
    #Si la letra no es ; la concateno
    r = ""
    for c in s:
        if c != ";":
            r = r + c
    return r



#CODIGO PRINCIPAL
#Entrada
sucio = input("Instruccion? ")

#Limpiar
limpio = sanitize(sucio)

#Salida
print("SUCIO:",sucio)
print("LIMPIO:",limpio)







