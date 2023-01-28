def verirut(rut,ver):
    #Convertir a int el rut
    rut = int(rut)
    #Si es k convertira a mayuscula
    if ver == "k":
        ver = "K"
    #Sacar digitos
    r = rut
    r1 = r % 10
    r = r // 10
    r2 = r % 10
    r = r // 10
    r3 =  r % 10
    r = r // 10
    r4 = r % 10
    r = r // 10
    r5 =  r % 10
    r = r // 10
    r6 = r % 10
    r = r // 10
    r7 =  r % 10
    r = r // 10
    r8 = r % 10
    #Calcular suma
    suma = ((r1*2) + (r2*3) + (r3*4) +
            (r4*5) + (r5*6) + (r6*7) +
            (r7*2) + (r8*3))

    #Divir 11 y obtener resto
    resto = suma % 11
    #Restar el resto
    res = 11 - resto
    #Verificador correcto
    if 1 <= res <= 9:
        vercor = str(res)
    elif res == 11:
        vercor = "0"
    elif res == 10:
        vercor = "K"

    return vercor == ver
    







'''
rut = input("Rut? ")
dv = input("Digito Verificador? ")

# Llamemos a mi colega 'verirut.
# Le damos el rut, le damos el digito
# verificador, y que nos responda
# si es correcto.

# Guardemos esa respuesta (True o False)
# en una variable llamada 'correcto'
# y sigamos con el programa

if correcto:
    print("RUT correcto")
else:
    print("RUT incorrecto")
'''



rut = input("Rut? ")
dv = input("Digito Verificador? ")

#Asi es como llamamos a mi colega verirut. 
#Para verirut el orden es muy importante:
#el primero el rut, y el segundo el digito verificador

correcto = verirut(rut,dv)

if correcto:
    print("RUT correcto")
else:
    print("RUT incorrecto")






    
