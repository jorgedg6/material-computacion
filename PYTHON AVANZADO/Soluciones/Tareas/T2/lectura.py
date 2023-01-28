import parametros as p
def leer(direccion):
    '''
    Lee archivos y los almacena en una lista de tuplas
    '''
    archivo = open(direccion, "r", encoding='utf-8')
    lectura = archivo.readlines()
    archivo.close()
    lista = []

    for linea in lectura:
        linea = linea.strip().split(',')
        lista.append((linea[0], int(linea[1])))
    return sorted(lista, key=sort, reverse=True)

def sort(elemento):
    '''
    Sort customizado para funcion leer
    '''
    return elemento[1]

def escribir(usuario, puntaje):
    '''
    Escribe en archivos
    '''
    archivo = open(p.RUTA_PUNTAJES, 'a', encoding='utf-8')
    archivo.write(f'{usuario},{puntaje}\n')
    archivo.close()