import lab

print("INI SYS CORONA")

continuar = True
while continuar:
    op = int(input("1-Abrir 2-Cerrar 0-Exit? "))

    if op == 0:
        continuar = False

    elif op == 1:
        edad = int(input("Edad? "))
        cid = lab.abrir(edad)
        print("Caso abierto con ID", cid)

    elif op == 2:
        cid = int(input("ID de Caso? "))
        res = int(input("Resultado 0-Neg 1-Pos? "))
        lab.cerrar(cid,res)

print("END SYS CORONA")




