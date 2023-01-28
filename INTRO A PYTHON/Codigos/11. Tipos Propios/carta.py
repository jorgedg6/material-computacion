class Carta:
    def __init__(self,p,n):
        self.pinta = p
        self.num = n

    def __str__(self):
        t = str(self.num) +"("+self.pinta+")"
        return t


def quien_gana(c1,c2):
    if c1.num > c2.num:
        r = 1
    elif c1.num < c2.num:
        r = 2
    elif c1.pinta == c2.pinta:
        r = 0
    elif c1.pinta == "rojo":
        r = 1
    else:
        r = 2
    return r



#TEST
'''
r5 = Carta("rojo",5)
print(r5)

r6 = Carta("rojo",6)
print(r6)

v6 = Carta("verde",6)
print(v6)
'''

'''
print(quien_gana(r5,r5))
print(quien_gana(r6,r5))
print(quien_gana(v6,r6))
print(quien_gana(v6,r5))
'''

r5 = Carta("rojo",5)
print(r5.pinta)
print(r5.num)

v6 = Carta("verde",6)
print(v6.pinta)
print(v6.num)

