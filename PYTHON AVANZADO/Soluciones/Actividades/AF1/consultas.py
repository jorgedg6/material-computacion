# --- EJEMPLO --- #
# [Plato1, Plato2, Plato2, Plato4]
# pasa a ser
# {"Categoria1": [Plato3, Plato2], "Categoria2": [Plato1, Plato4]}
def platos_por_categoria(lista_platos: list) -> dict:
    platos_categoria = {}
    categorias = set()
    for plato in lista_platos:
        categorias.add(plato.categoria)
    for categoria in categorias:
        platos_categoria[categoria] = []
    for plato in lista_platos:
        platos_categoria[plato.categoria].append(plato)
    #for plato in lista_platos:
    #    if plato[0] in platos_categoria:
    #        platos_categoria[plato[0]] = [plato]
    #    else:
    #        platos_categoria[plato[0]].append(plato)
    return platos_categoria
    pass


# Debe devolver los platos que no tengan ninguno de los ingredientes descartados
def descartar_platos(ingredientes_descartados: set, lista_platos: list):
    lista_platos_final = []
    for plato in lista_platos:
        estado = True
        for ingrediente in ingredientes_descartados:
            if ingrediente in plato.ingredientes:
                estado = False
        if estado:
            lista_platos_final.append(plato)
    return lista_platos_final
    pass


# --- EXPLICACION --- #
# Si el plato necesita un ingrediente que no tiene cantidad suficiente,
# entonces retorna False
#
# En caso que tenga todo lo necesario, resta uno a cada cantidad y retorna True
def preparar_plato(plato, ingredientes: dict) -> bool:
    for ingrediente_plato in plato.ingredientes:
        if ingredientes[ingrediente_plato] <= 0:
            return False

    for ingrediente_plato in plato.ingredientes:
        ingredientes[ingrediente_plato] -= 1

    return True


# --- EXPLICACION --- #
# Debe retornar un diccionario que agregue toda la información ...
#  de la lista de platos.
# precio total, tiempo total, cantidad de platos, platos
def resumen_orden(lista_platos: list) -> dict:
    precio_total = 0
    tiempo_total = 0
    nombres = []
    for plato in lista_platos:
        precio_total += plato.precio
        tiempo_total += plato.tiempo
        nombres.append(plato.nombre)
    resumen = {
        "precio total": precio_total,
        "tiempo total": tiempo_total,
        "cantidad de platos": len(lista_platos),
        "platos": nombres
    }
    return resumen
    pass

