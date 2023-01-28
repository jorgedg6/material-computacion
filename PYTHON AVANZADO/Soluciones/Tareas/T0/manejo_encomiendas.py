import menus
import lectura
from parametros import MAX_PESO

#Funcion que lee el input en caso de cancelar o continuar encomienda
def input_encomienda():
    print("\n[1] Continuar",
    "\n[2] Cancelar encomienda\n"
    )
    input_encomienda = input("\nIngrese selección: ")
    if input_encomienda == "1":
        return True
    elif input_encomienda == "2":
        return False
    else:
        print("\nRespuesta inválida, seleccione una de las opciones")
        input_encomienda()

#Funcion que verifica un nombre valido de la encomienda
#Llama a la funcion receptor encomienda y hereda el nombre de la encomienda
def nombre_encomienda(nombre_usuario):
    nombre = input("\n- Nombre de la encomienda: ")
    if "," in set(nombre):
        print("\n¡Dato ingresado en Nombre no cumple las normas! Desea:")
        valor = input_encomienda()
        if valor:
            nombre_encomienda(nombre_usuario)
            return None
        elif not valor:
            menus.menu_usuario(nombre_usuario)
            return None
    receptor_encomienda(nombre_usuario,nombre)

#Funcion que verifica un receptor valido de la encomienda
#Llama a la funcion peso encomienda y hereda el nombre y receptor de la encomienda
def receptor_encomienda(nombre_usuario, nombre):
    usuarios = lectura.compilar_usuarios("usuarios.csv")
    receptor = input("\n- Receptor de la encomienda: ")
    nombres = set()
    for usuario_previo in usuarios:
        nombres.add(usuario_previo[0])
    if receptor not in nombres:
        print("\n¡Dato ingresado en Receptor no cumple las normas! Desea:")
        valor = input_encomienda()
        if valor:
            receptor_encomienda(nombre_usuario,nombre)
            return None
        elif not valor:
            menus.menu_usuario(nombre_usuario)
            return None
    peso_encomienda(nombre_usuario,nombre,receptor)

#Funcion que verifica un peso valido de la encomienda
#Llama a la funcion destino encomienda y hereda el nombre, receptor y destino de la encomienda
def peso_encomienda(nombre_usuario, nombre, receptor):
    peso = float(input("\n- Peso de la encomienda: "))
    if peso > MAX_PESO:
        print("\n¡Dato ingresado en Peso no cumple las normas! Desea:")
        valor = input_encomienda()
        if valor:
            peso_encomienda(nombre_usuario, nombre, receptor)
            return None
        elif not valor:
            menus.menu_usuario(nombre_usuario)
            return None
    destino_encomienda(nombre_usuario, nombre, receptor, peso)

#Funcion que verifica un destino valido de la encomienda
#Manda a inscribir la encomienda en el archivo
#Llama a la funcion menu usuario
def destino_encomienda(nombre_usuario, nombre, receptor, peso):
    destino = input("\n- Destino de encomienda: ")
    if "," in set(destino):
        print("\n¡Dato ingresado en Destino no cumple las normas! Desea:")
        valor = input_encomienda()
        if valor:
            destino_encomienda(nombre_usuario,nombre,receptor,peso)
            return None
        elif not valor:
            menus.menu_usuario(nombre_usuario)
            return None
    indice = len(lectura.leer_encomiendas("encomiendas.csv"))
    lectura.agregar_encomienda_usuario("encomiendas_usuarios.csv", nombre_usuario, indice)
    lectura.agregar_encomienda("encomiendas.csv", nombre, receptor, peso, destino)
    menus.menu_usuario(nombre_usuario)

#Funcion que imprime las encomiendas
#Realiza la actualizacion de estado
#Manda a sobreescribir las encomiendas
def actualizar_encomiendas():
    encomiendas = lectura.leer_encomiendas("encomiendas.csv")
    print("\n--> Encomiendas registradas <--")
    print("\n", " "*25, "Nombre",
            " "*27, "Receptor",
            " "*8, "Peso",
            " "*9, "Destino",
            " "*14, "Estado\n")  
    for i in range(len(encomiendas)):
        print(f"[{i+1}] ",
            f"{encomiendas[i][0]:^50s}",
            f"{encomiendas[i][1]:^20s}",
            f"{encomiendas[i][2]:^10.1f}",
            f"{encomiendas[i][3]:^20s}",
            f"{encomiendas[i][5]:^25s}")
    print("\n[0] Volver")
    
    input_encomienda = input("\nIngrese selección: ")
    
    if input_encomienda == "0":
        menus.menu_administrador()
    elif not input_encomienda.isnumeric():
        print("\nRespuesta inválida, seleccione una de las opciones")
        actualizar_encomiendas()
    elif int(input_encomienda) > len(encomiendas) or int(input_encomienda) < 0:
        print("\nRespuesta inválida, seleccione una de las opciones")
        actualizar_encomiendas()
    else:
        encomienda_a_editar = encomiendas[int(input_encomienda)-1]
        estado = encomienda_a_editar[5]

        estados = ["Emitida", "Revisada por agencia", "En camino", "Llegada al destino"]
        
        if estado == estados[0]:
            encomiendas[int(input_encomienda)-1][5] = estados[1]
        elif estado == estados[1]:
            encomiendas[int(input_encomienda)-1][5] = estados[2]
        elif estado == estados[2]:
            encomiendas[int(input_encomienda)-1][5] = estados[3]
        elif estado == estados[3]:
            print("\nEsta encomienda ya ha llegado a su destino")
        
        lectura.sobreescribir_encomiendas("encomiendas.csv", encomiendas)
        if estado != "Llegada al destino":
            print("\nCambio realizado con éxito")
        menus.menu_administrador()

#Lee el archivo encomiendas_usuarios.py
#Retorna las encomiendas realizadas por el usuario de la sesión
def encomiendas_personales(nombre_usuario):
    print("\n-Encomiendas Realizadas-")
    encomiendas_usuario = lectura.leer_encomienda_usuario("encomiendas_usuarios.csv")
    encomiendas = lectura.leer_encomiendas("encomiendas.csv")
    i = 0
    print("\n", " "*25, "Nombre",
            " "*27, "Receptor",
            " "*8, "Peso",
            " "*9, "Destino",
            " "*14, "Estado\n") 
    estado = True
    for encomienda_usuario in encomiendas_usuario:
        if encomienda_usuario[0] == nombre_usuario:
            estado = False
            print(f"\n[{i+1}] ",
                f"{encomiendas[int(encomienda_usuario[1])][0]:^50s}",
                f"{encomiendas[int(encomienda_usuario[1])][1]:^20s}",
                f"{encomiendas[int(encomienda_usuario[1])][2]:^10.1f}",
                f"{encomiendas[int(encomienda_usuario[1])][3]:^20s}",
                f"{encomiendas[int(encomienda_usuario[1])][5]:^25s}",
            )
            i += 1
    if estado:
        print("\nNo has realizado ninguna encomienda")
    input("\nPresione enter para regresar")
    menus.menu_usuario(nombre_usuario)

#Funcion que lee las encomiendas
#Retorna los pedidos del usuario de la sesion
def pedidos_personales(nombre_usuario):
    encomiendas = lectura.leer_encomiendas("encomiendas.csv")
    print("\n-Pedidos personales-")
    i = 0
    print("\n", " "*25, "Nombre",
            " "*27, "Receptor",
            " "*8, "Peso",
            " "*9, "Destino",
            " "*14, "Estado\n") 
    for encomienda in encomiendas:
        if encomienda[1] == nombre_usuario:
            print(f"[{i+1}] ",
                    f"{encomienda[0]:^50s}",
                    f"{encomienda[1]:^20s}",
                    f"{encomienda[2]:^10.1f}",
                    f"{encomienda[3]:^20s}",
                    f"{encomienda[5]:^25s}")
            i += 1
    input("\nPresione enter para regresar")
    menus.menu_usuario(nombre_usuario)