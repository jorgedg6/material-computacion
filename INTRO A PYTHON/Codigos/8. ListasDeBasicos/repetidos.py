#Lista de palabras (inicialmente vacia)
ps = [] 

#Pedir letra
let = input("Letra: ")
let = let.upper()

continuar = True
while continuar:

    #Pedir palabra
    p = input("Palabra: ")
    
    # En mayusculas, para estandarizar
    p = p.upper()

    if not (let in p):
        print("La palabra NO tiene", let)
        continuar = False

    elif p in ps:
        print("Has repetido",p)
        continuar = False

    else:
        print("Bien!")
        ps.append(p)

print("Juego acabado")




