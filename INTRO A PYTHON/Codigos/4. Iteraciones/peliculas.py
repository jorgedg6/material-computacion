np = int(input("Cuantas personas somos? "))
nm = int(input("Cuantas peliculas por persona? "))

for i in range(0,np):
    print("--------Persona",i,"Di tus",nm,"peliculas.")

    for j in range(0,nm):
        m = input("Peli? ")
        print("=>",m,"Me la apunto.")

print("Muchas gracias a todos.")



