class Hogar:
    def __init__(self,ms,ing,gas):
        self.ms = ms
        self.ing = ing
        self.gas = gas


#TEST
h1 = Hogar(1,1000,2000)
h2 = Hogar(2,0,1500)
h3 = Hogar(2,1000,1200)
h4 = Hogar(1,1000,200)


# Informacion de hogares sacada
# de alguna base de datos publica
# como datos.gov.cl


hogares = [h1,h2,h3,h4]

num = 0
for h in hogares:
    ep = (h.gas-h.ing) / h.ms
    if ep >= 500:
        num += 1

print(num, "de",len(hogares), "hogares tienen superior a 500") 
        

