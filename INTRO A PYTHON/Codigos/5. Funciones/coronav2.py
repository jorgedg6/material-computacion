import lab

print("INI SYS CORONA")

continuar = True
while continuar:
    op = int(input("1-Abrir 2-Cerrar 3-Reportes 0-Exit? "))

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

    elif op == 3:
        opr = int(input("0-R.Casos 1-R.J/V? "))

        if opr == 0:
            ncs = lab.ncasos()
            for i in range(0,ncs):
                edad = lab.edad(i)
                res = lab.resultado(i)
                print("ID",i,edad,res)

        elif opr == 1:
            ncj = 0
            ncv = 0
            npj = 0
            npv = 0

            ncs = lab.ncasos()
            for i in range(0,ncs):
                edad = lab.edad(i)
                res = lab.resultado(i)

                if edad <= 50: #Jovenes
                    if res != -1: #Hay resultado
                        ncj += 1
                        if res == 1: #Es positivo
                            npj += 1
                else:         #Viejos
                    if res != -1: #Hay resultado
                        ncv += 1
                        if res == 1: #Es positivo
                            npv += 1

            print("Jovenes:",npj,"/",ncj)
            print("Viejos (+50):",npv,"/",ncv)
            
print("END SYS CORONA")


