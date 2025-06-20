print ("DÍAS DE LA SEMANA")
print("-------------------")
print ("1.-Lunes")
print ("2.-Martes")
print ("3.-Miercoles")
print ("4.-Jueves")
print ("5.-Viernes")
print ("6.-Sabado")
print ("7.-Domingo")
dia = int(input("ingrese un dia: "))

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("Numero Invalido")