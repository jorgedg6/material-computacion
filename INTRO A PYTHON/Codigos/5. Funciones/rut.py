# Nombre 'limpiar'

# Recibe un str con el rut sucio
# (con/sin puntos, guion, espacios, k/K, ...)

# Retorna un str con el rut limpio
# (xx.xxx.xxx-y)


def limpiar(sucio):
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





