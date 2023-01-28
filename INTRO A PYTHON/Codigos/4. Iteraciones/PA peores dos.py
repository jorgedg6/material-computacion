num = int(input("Cuantas notas? "))

penultima = 8.0
ultima = 8.0
suma = 0

for i in range(0,num):
    
    print("NOTA",i)
    n = float(input("Nota? "))
    suma = suma + n

    if n < penultima and n >= ultima:
        penultima = n
    elif n < ultima:
        penultima = ultima
        ultima = n



promedio = (suma - penultima - ultima) / (num - 2)
print("Mi promedio es", promedio)

