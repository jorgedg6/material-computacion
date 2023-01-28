Ra = int(input("Puntos A: "))
Rb = int(input("Puntos B: "))

#A gana. K es 25
Ea = 1 / (1 +  (10** ((Rb-Ra)/400)) )
Eb = 1 / (1 +  (10** ((Ra-Rb)/400)) )
nRa = Ra + 25*(1-Ea)
nRb = Rb + 25*(0-Eb)

print("Nuevos puntos A: ",nRa)
print("Nuevos puntos B: ",nRb)
    
    



