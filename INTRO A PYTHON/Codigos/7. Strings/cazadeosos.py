'''CAZA DE OSOS
Funcion que cuenta cuantas veces aparece OSO hacia abajo, hacia el lado derecho, en diagonal hacia abajo
Entrada: string x, y, z, de misma longitud 'n' (>=3) compuestos por las letras 'O' y 'S'
Salida: int con el numero de veces
'''

def contar_osos(x,y,z):
    n = len(x)
    num = 0

    #Horizontal
    for i in range(0,n-2):
        if x[i]+x[i+1]+x[i+2] == "OSO":
            num += 1
        if y[i]+y[i+1]+y[i+2] == "OSO":
            num += 1
        if z[i]+z[i+1]+z[i+2] == "OSO":
            num += 1

    #Vertical
    for i in range(0,n):
        if x[i]+y[i]+z[i] == "OSO":
            num += 1

    #Diagonal
    for i in range(0,n-2):
        if x[i]+y[i+1]+z[i+2] == "OSO":
            num += 1

    return num
    
    

#CODIGO PRINCIPAL (TEST)
x = "OOSOS"
y = "SSOSO"
z = "OOOSO"

num = contar_osos(x,y,z)
print(num)
      
    

