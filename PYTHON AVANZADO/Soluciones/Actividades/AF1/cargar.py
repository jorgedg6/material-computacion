import collections
# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,categoria,tiempo_preparacion,precio,ingrediente_1,...,ingrediente_n
def cargar_platos(ruta_archivo: str) -> list:
    #Abrimos el archivo
    archivo = open(ruta_archivo,"r")
    platos_txt = archivo.readlines()
    platos = []

    #Armamos el Tuple
    Plato = collections.namedtuple('Plato_type',['nombre','categoria','tiempo','precio','ingredientes'])

    #Cargamos las lineas
    for linea in platos_txt:
        linea = linea.strip('\n').split(',')
        ingredientes = set(linea[4].split(';'))
        platos.append(Plato(linea[0],linea[1],int(linea[2]),int(linea[3]),ingredientes))
    return platos
    pass


# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,cantidad
def cargar_ingredientes(ruta_archivo: str) -> dict:

    #Abrimos el archivo
    archivo = open(ruta_archivo,"r")
    ingredientes_txt = archivo.readlines()
    ingredientes = {}

    #Guardamos las lineas en el diccionario
    for linea in ingredientes_txt:
        linea = linea.strip('\n').split(',')
        ingredientes[linea[0]] = int(linea[1])
    return ingredientes
    pass
