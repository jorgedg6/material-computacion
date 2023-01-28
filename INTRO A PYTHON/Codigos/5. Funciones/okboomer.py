def dosdig(rut):
    d = rut // 1000000
    return d

n1 = input("Nombre Personaje 1? ")
r1 = int(input("RUT de "+n1+"? "))

n2 = input("Nombre Personaje 2? ")
r2 = int(input("RUT de "+n2+"? "))

d1 = dosdig(r1)
d2 = dosdig(r2)

if d1 < d2:
    v = n1
    j = n2
else:
    v = n2
    j = n1

print("- Maldito milenial! - dijo",v,"gritando.")
print("- Lo que tu digas boomer - respondio",j,"irrespetuosamente.")

