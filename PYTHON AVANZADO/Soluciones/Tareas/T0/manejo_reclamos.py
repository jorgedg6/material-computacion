import lectura
import menus

#Funcion que crea un reclamo
#Llama a la funcion menu usuario
def crear_reclamo(nombre_usuario):
    titulo = input("Título del reclamo: ")
    descripcion = input("Cuerpo del reclamo: ")
    lectura.agregar_reclamo("reclamos.csv",nombre_usuario,titulo,descripcion)
    print("\nReclamo enviado con éxito")
    menus.menu_usuario(nombre_usuario)

#Funcion recursiva que permite revisar reclamos
#Llama a la funcion menu administrador
def revisar_reclamos():
    reclamos = lectura.leer_reclamos("reclamos.csv")
    print("\n--> Buzón de reclamos <--")
    print("\n-Elija uno de los siguientes reclamos para visualizar su descripción-\n\n")
    for i in range(1,len(reclamos)):
        print(f"[{i}] {reclamos[i][1]}")
    print("\n[0] Volver")
    input_reclamo = int(input("\nIngrese selección: "))
    if input_reclamo == 0:
        menus.menu_administrador()
    elif int(input_reclamo) >= len(reclamos):
        print("Seleccione una opción válida")
    else:
        print("\n  -Reclamo-")
        print(f"\n\n- Título: {reclamos[input_reclamo][1]}",
        f"\n- Descripción: {reclamos[input_reclamo][2]}")
        print("\nPara volver presione cualquier tecla")     
        input_reclamo = input()
        revisar_reclamos()