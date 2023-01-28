def limpiar(sucio):
    r = ""
    for c in sucio:
        if c in "0123456789":
            r += c
        elif c in "kK":
            r += "K"
    s = r[:2]+"."+r[2:5]+"."+r[5:8]+"-"+r[8:]
    return s

r = open("rutssucios.txt")
ls = r.readlines()
r.close()

e = open("rutslimpios.txt","w")
for l in ls:
    sucio = l.strip()
    limpio = limpiar(sucio)
    print(limpio,file=e)
e.close()


