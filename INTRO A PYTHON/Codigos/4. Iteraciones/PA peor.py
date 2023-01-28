num = int(input("Cuantas notas? "))

peor = 8.0
suma = 0

for i in range(0,num):
    print("NOTA",i)
    n = float(input("Nota? "))
    suma = suma + n

    if n < peor:
        peor = n

promedio = (suma - peor) / (num - 1)
print("Mi promedio es", promedio)

