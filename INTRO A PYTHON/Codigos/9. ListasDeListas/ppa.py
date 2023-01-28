def ppa(es):
    
    #Creo una lista donde pondre listas ([nombre,ppa])
    datos = []

    #Miro estudiante a estudiante
    for e in es:
        nombre = e[0]
        notas = e[1]

        #Calculo el promedio(ppa)
        suma = 0
        for n in notas:
            suma += n
        ppa = suma / len(notas)

        #Creo una lista 
        dato = [nombre,ppa]

        #La agrego a mi lista de datos
        datos.append(dato)

    #Retornar
    return datos


#CODIGO PRINCIPAL (TEST)

es = [["Alice",[6.6,5.4,6.0]],
      ["Barto",[4.0,4.0]],
      ["Carlo",[5.5,6.2,6.9,7.0]],
      ["Peter",[5.5,4.3]]]

ppas = ppa(es)
print(ppas)



           



        

