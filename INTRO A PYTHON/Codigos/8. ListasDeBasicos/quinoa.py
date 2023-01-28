ns = ["X","X","X","X","X"]
hs = [0 ,0 ,0 ,0 ,0]

print("HELLO")

continuar = True
while continuar:
    op = int(input("1-Nueva 2-Eliminar 3-Hojas 4-Mostrar 0-Salir: "))

    if op == 0:
        continuar = False

    elif op == 1:
        s = int(input("Maceta? "))
        n = input("Tipo: (B-Blanca N-Negra R-Rojas)? ")
        ns[s] = n

    elif op == 2:
        s = int(input("Maceta? "))
        ns[s] = "X"
        hs[s] = 0

    elif op == 3:
        s = int(input("Maceta? ")) 
        if ns[s] == "X":
            print("ERROR: No hay planta")
        else:
            h = int(input("Hojas? "))
            hs[s] = h

    elif op == 4:
        print(ns[0],ns[1],ns[2],ns[3],ns[4])
        print(hs[0],hs[1],hs[2],hs[3],hs[4])


print("CIAO")



