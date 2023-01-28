from datetime import datetime

#Lee el archivo usuarios.csv y retorna una
#lista de tuplas con el formato (usuario, contraseña)
def compilar_usuarios(direccion):
    archivo = open(direccion, "r", encoding='utf-8')
    usuarios_sucio = archivo.readlines()
    usuarios_limpio = []
    archivo.close()
    for usuario in usuarios_sucio[1:]:
        usuario = usuario.strip("\n").split(",")
        usuarios_limpio.append((usuario[0], usuario[1]))
    return usuarios_limpio

#Agrega un usuario al archivo usuarios.csv
def agregar_usuario(direccion, nombre, contrasena):
    archivo = open(direccion, "a", encoding='utf-8')
    archivo.write(f"\n{nombre},{contrasena}")
    archivo.close()

#Lee el archivo encomiendas.csv y retorna una
#lista de listas con el formato [Nombre, Receptor, Peso, Destino, Fecha, Estado]
def leer_encomiendas(direccion):
    archivo = open(direccion, "r", encoding='utf-8')
    encomiendas_sucio = archivo.readlines()
    encomiendas_limpio = []
    archivo.close()

    for encomienda in encomiendas_sucio[1:]:
        encomienda = encomienda.strip("\n").split(",")
        encomiendas_limpio.append([encomienda[0],encomienda[1],float(encomienda[2]),
        encomienda[3],encomienda[4],encomienda[5]])
    return encomiendas_limpio

#Agrega una encomienda al archivo encomiendas.csv
def agregar_encomienda(direccion, nombre, receptor, peso, destino):
    archivo = open(direccion, "a", encoding='utf-8')
    archivo.write(f"\n{nombre},{receptor},{peso},{destino},{datetime.today().strftime('%Y/%m/%d %H:%M:%S')},Emitida")
    archivo.close()
    print("\nEncomienda creada con éxito")

#Actualiza el archivo encomiendas.csv con el estado actualizado
#Se hace utilizacion de la abreviacion obj[] para agilizar la escritura
#Debe agregar los títulos antes ya que obtiene la lista limpia de encomiendas
#que retorna leer_encomiendas(dirección)
def sobreescribir_encomiendas(direccion, lista):
    archivo = open(direccion, "w", encoding='utf-8')
    archivo.write("nombre_articulo,receptor,peso,destino,fecha,estado")
    for obj in lista:
        archivo.write(f"\n{obj[0]},{obj[1]},{obj[2]},{obj[3]},{obj[4]},{obj[5]}")
    archivo.close()

#Lee el archivo reclamos.csv, y retorna una lista de
#tuplas con el formato (Usuario, Título, Descripción)
def leer_reclamos(direccion):
    archivo = open(direccion, "r", encoding='utf-8')
    reclamos_sucio = archivo.readlines()
    reclamos_limpio = []
    archivo.close()
    
    for reclamo in reclamos_sucio[1:]:
        reclamo = reclamo.strip("\n")
        comas = 0
        i = 0
        for caracter in reclamo:
            if caracter == ",":
                comas += 1
                if comas == 2:
                    indice = i
            i += 1
        reclamo2 = reclamo[:indice]
        reclamo2 = reclamo2.split(",")
        reclamo2.append(reclamo[indice + 1:])
        reclamos_limpio.append((reclamo2[0], reclamo2[1], reclamo2[2]))
    return reclamos_limpio

#Agrega un reclamo al archivo reclamos.csv
def agregar_reclamo(direccion, usuario, titulo, cuerpo):
    archivo = open(direccion, "a", encoding='utf-8')
    archivo.write(f"\n{usuario},{titulo},{cuerpo}")
    archivo.close()

#Lee el archivo encomiendas_usuarios.csv
#Retorna una lista de tuplas con el formato (Usuario,Índice encomienda)
def leer_encomienda_usuario(direccion):
    archivo = open(direccion, "r", encoding='utf-8')
    encomiendas_sucio = archivo.readlines()
    encomiendas_limpio = []
    archivo.close()

    for encomienda in encomiendas_sucio[1:]:
        encomienda = encomienda.strip("\n").split(",")
        encomiendas_limpio.append((encomienda[0], encomienda[1]))
    return encomiendas_limpio

#Agrega una encomienda al arrchivo encomiendas_usuarios.csv
def agregar_encomienda_usuario(direccion, usuario, indice):
    archivo = open(direccion, "a", encoding='utf-8')
    archivo.write(f"\n{usuario},{indice}")
    archivo.close()

#Coloca el encabezado del archivo encomiendas_usuarios.csv
#para facil entendimiendo de su formato
def inicializar_encomiendas_usuarios(direccion):
    archivo = open(direccion, "w", encoding='utf-8')
    archivo.write(f"usuario,indice")
    archivo.close()