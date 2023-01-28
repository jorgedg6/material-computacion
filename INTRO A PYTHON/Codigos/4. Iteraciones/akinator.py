m = int(input("Numero de intentos maximos? "))
acertado = False
i = 0

while (not acertado) and i < m:
    print("##Haz la pregunta", i)

    lose = int(input("¿Lo sabes? 0-No 1-Sí? "))
    if lose == 0:
        i += 1

    elif lose == 1:
        print("##Di que personaje crees que es")
        leachunte = int(input("¿Le achuntaste? 0-No 1-Sí? "))
        if leachunte == 1:
            acertado = True
        elif leachunte == 0:
            i += 1

if acertado:
    print("FELICIDADES")
    print("Necesitaste",i+1,"intentos")
elif i == m:
    print("Te quedaste sin intentos :(")



            
            
                
