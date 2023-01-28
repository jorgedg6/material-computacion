import lectura
from parametros import MIN_CARACTERES, LARGO_CONTRASENA, CONTRASENA_ADMIN
import menus

#Funcion que verifica el usuario, recibe direccion del archivo
#Llama a la funcion inicio si el input es erroneo
#Llama a la funcion menu de usuario si el input es correcto
def verificar_usuario(direccion):
    nombre_usuario = input("\nNombre de Usuario: ")
    usuarios = lectura.compilar_usuarios(direccion)
    nombres = set(usuarios[i][0] for i in range(len(usuarios)))
    if nombre_usuario not in nombres:
        print("\nUsuario inválido")
        menus.menu_inicio()
    else:
        contrasena = input("\nContraseña: ")
        contrasenas = set(usuarios[i][1] for i in range(len(usuarios)))
        if contrasena not in contrasenas:
            print("\nUContraseña inválida")
            menus.menu_inicio()
        else:
            print("\nInicio de sesión exitoso")
            menus.menu_usuario(nombre_usuario)

#Funcion que verifica el nuevo usuario, recibe direccion del archivo
#Llama a la funcion inicio si el input es erroneo
#Llama a la funcion verificar contraseña si el input es correcto
def verificar_nuevo_usuario(direccion):
    nombre_usuario = input("\nNombre de Usuario: ")
    suma = 0
    for i in range(len(nombre_usuario)):
        if nombre_usuario[i].isalpha(): #alfabeticos
            suma += 1
    if suma < MIN_CARACTERES:
        print("\nNombre de usuario inválido,",
        f"debe tener un mínimo de {MIN_CARACTERES} caracteres alfabéticos")
        menus.menu_inicio()
        return None
    usuarios = lectura.compilar_usuarios(direccion)
    for usuario_previo in usuarios:
        if nombre_usuario[0] == usuario_previo[0]:
            print("\nNombre de usuario inválido, nombre ya está en uso")
            menus.menu_inicio()
            return None
    verificar_contrasena(nombre_usuario)

#Funcion que verifica la nueva contraseña, recibe el nombre de usuario
#Llama a la funcion recursiva si el input es erroneo
#Llama a la funcion inscribir usuario si el input es correcto
def verificar_contrasena(nombre_usuario):
    contrasena = input("\nContraseña: ")
    if len(contrasena) < LARGO_CONTRASENA:
        print("\nContraseña inválida, debe tener un mínimo de 6 caracteres")
        verificar_contrasena(nombre_usuario)
        return None
    for i in range(len(contrasena)):
        if not contrasena[i].isnumeric() and not contrasena[i].isalpha():
            print("\nContraseña inválida, sólo debe tener caracteres alfanuméricos")
            verificar_contrasena(nombre_usuario)
            return None
    inscribir_usuario(nombre_usuario,contrasena)

#Funcion que incribe el nuevo usuario al archivo usuarios.csv
#Llama a la funcion menu usuario
def inscribir_usuario(nombre_usuario, contrasena):
    lectura.agregar_usuario("usuarios.csv", nombre_usuario, contrasena)
    print("\nUsuario inscrito exitósamente")
    menus.menu_usuario(nombre_usuario)

#Funcion que verifica la contraseña del admin
#Ofrece introducir nueva contraseña en base a su recursividad
#LLama a la funcion menu administrador
def verificar_admin():
    contrasena = input("\nContraseña: ")
    if contrasena == CONTRASENA_ADMIN:
        print("\nInicio de sesión exitoso")
        menus.menu_administrador()
    else:
        print("\nContraseña errónea ¿Desea volver a ingresar una contraseña?: ")
        print(
            "\n[1] Sí",
            "\n[2] No\n"
        )
        input_usuario = input("\nIngrese selección: ")
        if input_usuario == "1":
            verificar_admin()
        elif input_usuario == "2":
            menus.menu_inicio()
        else:
            print("\nRespuesta inválida, seleccione una de las opciones")
            verificar_admin()