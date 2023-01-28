compra = [["Aceite",3500],["Pasta",1300],["Arroz",980],["Pollo",2340]]

# Producto en la posicion 2 de la lista de la compra
prod = compra[2] 
# Su Nombre y precio
nombre = prod[0]
precio = prod[1]


# Puedes encadenarlo para ir mas directo
# compra[2] es una lista, no? pues a una lista le puedes
# poner el [] pegado para acceder a un elemento. 
# Es exactamente LO MISMO de siempre
nombre = compra[2][0]
precio = compra[1][1]


# Lo mismo con listas de listas de listas, ...
qs = [["USA",["MIT","Harvard","Stanford"]],
        ["UK",["Oxford","Cambridge"]],
        ["Japan",["Todai","Sokendai"]]]

#El nombre de la primera universidad de USA
top = qs[0][1][0]

#La larga
usa = qs[0] #Lista [str,list]
unis = usa[1] # Lista de str con las unis
top = unis[0] # str con la top uni (pos 0)




           



        

