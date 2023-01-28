def leer(direccion):
    archivo = open(direccion, "r", encoding='utf-8')
    lectura = archivo.readlines()
    archivo.close()

    lista = []
    llaves = lectura[0].strip("\n").strip("\r").replace(" ", "_").split(",")
    for linea in lectura[1:]:
        diccionario = {}
        linea = linea.strip("\n").strip("\r").split(",")
        for i in range(len(llaves)):
            if linea[i].isnumeric():
                diccionario[llaves[i]] = int(linea[i])
            else:
                diccionario[llaves[i]] = linea[i]
        lista.append(diccionario)
    return lista