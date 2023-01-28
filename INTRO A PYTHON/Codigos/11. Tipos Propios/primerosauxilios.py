class Atenciones:
    def __init__(self):
        self.noms = []
        self.atens = []

    def nueva_atencion(self,nom,aten):
        self.noms.append(nom)
        self.atens.append(aten)

    def num_atenciones(self,nom):
        res = 0
        for n in self.noms:
            if n == nom:
                res += 1
        return res

    def atendido(self,nom):
        num = self.num_atenciones(nom)
        if num == 0:
            res = False
        else:
            res = True
        return res

    def multiples(self):
        #Nombres sin repetidos
        norep = []
        for n in self.noms:
            if n not in norep:
                norep.append(n)

        multiples = []
        for n in norep:
            if self.num_atenciones(n) >= 2:
                multiples.append(n)
        return multiples


print("APP Ini")
ats = Atenciones()

continuar = True
while continuar:
    op = int(input("1-Nueva Atencion 2-Num Atenciones, 3-Atendido 4-Multiples 0-Salir: "))
    if op == 0:
        continuar = False
    elif op == 1:
        n = input("Nombre? ")
        a = input("Descripcion de la Atención? ")
        ats.nueva_atencion(n,a)
    elif op == 2:
        n = input("Nombre? ")
        num = ats.num_atenciones(n)
        print("El numero de atenciones de",n,"es",num)
    elif op == 3:
        n = input("Nombre? ")
        res = ats.atendido(n)
        print(n," ha sido atendido:", res)
    elif op == 4:
        mul = ats.multiples()
        print("Personas con multiples atenciones",mul)
        
print("APP End")
                
    
        
        

