#Entrada
pos = int(input("Tu posicion? "))
posr = int(input("Posicion del ganador Copa del Rey? "))

#Europa si ... (soy los 6 primeros) o (gano Rey) o (soy 7 y el rey de los 6 primeros) 
europa = (pos <= 6) or (pos == posr) or (pos == 7 and posr <= 6) 

#Salida
print("Jugaremos en europa:",europa)


