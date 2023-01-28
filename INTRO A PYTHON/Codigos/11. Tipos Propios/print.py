class Carta:
    def __init__(self,p,n):
        self.pinta = p
        self.num = n

    
    def __str__(self):
        t = "El " + str(self.num) + " de "+self.pinta
        return t
    
'''
n = 5
print(n)

s = "hola"
print(s)

p = ["adios",8,"mundo"]
print(p)
'''

c1 = Carta("corazones",7)
print(c1)

c2 = Carta("rombos", 2)
print(c2)



