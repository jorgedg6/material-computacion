r = open("2020-06-08-CasosConfirmados.csv", encoding="utf-8")
ls = r.readlines()
r.close()

region = input("Codigo Region? ")

suma = 0
for l in ls:
    cs = l.strip().split(",")
    if cs[1] == region:
        casos = float(cs[5])
        suma += casos
        
print("Region",region,"-",suma),








