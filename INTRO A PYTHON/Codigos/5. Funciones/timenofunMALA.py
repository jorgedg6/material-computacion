#IDA
ida_h = int(input("IDA Horas: "))
ida_m = int(input("IDA Minutos: "))
ida_s = int(input("IDA Segundos: ")
ida = ida_h * 3600
ida = ida + (ida_m * 60)
ida = ida + ida_s
print("IDA:", ida_s, "segundos")

#UNI
uni_h = int(input("UNI Horas: "))
uni_m = int(input("UNI Minutos: "))
uni_s = int(input("UNI Segundos: "))
uni = uni_h * 3600
uni = uni + (uni_m * 60)
uni = uni + ida_s
print("UNI:", ida, "segundos")


#VUELTA
vue_h = int(input("VUELTA Horas: "))
vue_m = int(input("VUELTA Minutos: "))
vue_s = int(input("VUELTA Segundos: "))
vue = vue_h * 360
vue = vue + (vue_m * 60)
vue = vue + vue_s
print("UNI:", vue, "segundos")

