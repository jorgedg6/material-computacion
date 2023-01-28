#Entrada
t = input("Texto: ")
p = input("Palabra: ")

#Crear palabra inversa
inv = ""
for c in p:
    inv = c + inv

#Ver si la palabra y/o inversa estan
if (p in t) and (inv in t):
    print("ALERTA: palabra e inverso en texto")
elif (p in t) and not (inv in t):
    print("ALERTA: palabra en texto")
elif not (p in t) and (inv in t):
    print("ALERTA: inverso en texto")
else:
    print("Texto LIMPIO")

