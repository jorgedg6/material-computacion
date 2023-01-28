import criptografia
import manejo_encomiendas
import manejo_reclamos

#Funcion recursiva de menu de inicio
def menu_inicio():
    print("\n---> Menú de inicio <---")
    print("\nSelecciona una de las siguientes opciones:")
    print(
        "\n[1] Iniciar sesión como usuario",
        "\n[2] Registrarse como usuario",
        "\n[3] Iniciar sesión como administrador",
        "\n[4] Salir del programa\n"
        )
    #Input usuario
    input_usuario = input("\nIngrese selección: ")

    if input_usuario == "1":
        criptografia.verificar_usuario("usuarios.csv")    
    elif input_usuario == "2":
        criptografia.verificar_nuevo_usuario("usuarios.csv")
    elif input_usuario == "3":
        criptografia.verificar_admin()
    elif input_usuario == "4":
        print("\n¡Adiós, esperamos verte pronto!")
    else:
        print("\nRespuesta inválida, seleccione una de las opciones")
        menu_inicio()

#Funcion recursiva de menu de usuario
def menu_usuario(nombre_usuario):
    print("\n--> Menú de Usuario <--")
    print("\nSelecciona una de las siguientes opciones:")
    print(
        "\n[1] Hacer encomienda",
        "\n[2] Revisar estado de encomiendas realizadas",
        "\n[3] Realizar reclamos",
        "\n[4] Ver el estado de pedidos personales",
        "\n[5] Cerrar Sesión\n"
        )
    #Input usuario
    input_usuario = input("\nIngrese selección: ")

    if input_usuario == "1":
        manejo_encomiendas.nombre_encomienda(nombre_usuario)
    elif input_usuario == "2":
        manejo_encomiendas.encomiendas_personales(nombre_usuario)
    elif input_usuario == "3":
        manejo_reclamos.crear_reclamo(nombre_usuario)
    elif input_usuario == "4":
        manejo_encomiendas.pedidos_personales(nombre_usuario)
    elif input_usuario == "5":
        print("\nSesión cerrada con éxito")
        menu_inicio()
    else:
        print("\nRespuesta inválida, seleccione una de las opciones")
        menu_usuario(nombre_usuario)

#Funcion recursiva de menu de administrador
def menu_administrador():
    print("\n--> Menú de Administrador <--")
    print("\nSelecciona una de las siguientes opciones:")
    print(
        "\n[1] Actualizar encomiendas",
        "\n[2] Revisar reclamos",
        "\n[3] Cerrar Sesión\n"
        )
    #Input usuario
    input_usuario = input("\nIngrese selección: ")

    if input_usuario == "1":
        manejo_encomiendas.actualizar_encomiendas()
    elif input_usuario == "2":
        manejo_reclamos.revisar_reclamos()
    elif input_usuario == "3":
        print("\nSesión cerrada con éxito")
        menu_inicio()
    else:
        print("\nRespuesta inválida, seleccione una de las opciones")
        menu_administrador()