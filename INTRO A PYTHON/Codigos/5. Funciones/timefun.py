def tiempear(etapa):
    h = int(input(etapa + " Horas: "))
    m = int(input(etapa + " Minutos: "))
    s = int(input(etapa + " Segundos: "))
    r = h * 3600
    r = r + (m * 60)
    r = r + s
    return r


#IDA
ida = tiempear("IDA")
print("IDA:", ida, "segundos")
#UNI
uni = tiempear("UNI")
print("UNI:", uni, "segundos")
#VUELTA
vue = tiempear("VUELTA")
print("VUELTA:",vue, "segundos")


