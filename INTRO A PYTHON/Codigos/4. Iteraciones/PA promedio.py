num = int(input("Cuantas notas? "))

suma = 0
for i in range(0,num):
    print("NOTA",i)
    n = float(input("Nota? "))
    suma = suma + n

promedio = suma / num
print("Mi promedio es", promedio)

