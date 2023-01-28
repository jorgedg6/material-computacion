# OPEN - READLINE - CLOSE
r = open("notasI1.txt")
ls = r.readlines()
r.close()

# 'ls' es una list de str
# donde cada elemento es una linea del archivo
nest = 0
suma = 0
for l in ls:
    nota = float(l)
    if nota != 1.0:
        nest += 1
        suma += nota

print("Promedio:",suma/nest)












