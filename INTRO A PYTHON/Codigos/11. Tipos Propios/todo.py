class TODO:
    def __init__(self):
        self.tas = []
        self.tbs = []

    def agregar(self,t,p):
        if p == "alta":
            self.tas.append(t)
        elif p == "baja":
            self.tbs.append(t)

    def que_hacer(self):
        if len(self.tas) > 0:
            r = self.tas.pop(0)
        elif len(self.tbs) > 0:
            r = self.tbs.pop(0)
        else:
            r = "NADA"
        return r

    def __str__(self):
        txt = "--ALTA--\n"
        for t in self.tas:
            txt = txt + t + "\n"
        txt += "--BAJA--\n"
        for t in self.tbs:
            txt = txt + t + "\n"
        return txt


#CODIGO PRINCIPAL
todo = TODO()

continuar = True
while continuar:
    op = int(input("1-Agregar 2-Que Hacer 3-Mostrar 0-Salir: "))

    if op == 0:
        continuar = False
        
    elif op == 1:
        t = input("Tarea: ")
        p = input("Prioridad (alta/baja): ")
        todo.agregar(t,p)
        
    elif op == 2:
        t = todo.que_hacer()
        print("Hacer ->",t)

    elif op == 3:
        print(todo)
        
        

