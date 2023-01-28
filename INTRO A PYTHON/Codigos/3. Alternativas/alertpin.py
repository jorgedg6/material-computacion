#Entradas
azucar = int(input("Azucar: "))
pulso = int(input("Pulso: "))

#bool que me dice si el azucar es normal
azucar_normal = azucar >= 70 and azucar <= 145
#bool que me dice si el pulso es normal
pulso_normal = pulso >= 60 and pulso <= 100


if azucar_normal and pulso_normal:
    print("VERDE")
elif azucar_normal and not pulso_normal:
    print("AMARILLO")
elif not azucar_normal and pulso_normal:
    print("AMARILLO")
elif not azucar_normal and not pulso_normal:
    print("ROJO")




    

