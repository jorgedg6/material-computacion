# Input (String)
nombre = input("Introduce tu nombre: ")
type(nombre) # Siempre es str
print("Tu nombre es", nombre)

# Input (Numero)
edad = input("Introduce tu edad: ")
type(edad) # Siempre es str
print("Tu edad es", edad)
# edad_siguiente = (edad+1) #ERROR
edad_siguiente = int(edad) + 1
print("Edad siguiente es", edad_siguiente)

#O hacer conversion directa
nota = float(input("Tu nota: "))
reprobado = (nota < 4.0)
print("Has reprobado=>", reprobado)



