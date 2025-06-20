bono = 0
subsidio = 0
bonoedad = 0
total = 0

while True:
    nivel = int (input("ingrese su nivel socioeconomico del 1-5: "))
    print(" ")
    print("1.-Empleado")
    print("2.-Desempleado")
    cond = int(input("ingrese la opcion de su situacion laboral 1 o 2: "))
    print(" ")
    edad = int (input("ingrese su edad: "))
    if nivel > 0 and nivel < 6 and cond >= 1 and cond <= 2 and edad > 0:
        if nivel == 1 or nivel == 2:
            bono = 50_000
            if cond == 1:
                subsidio = 250_000
                total = subsidio+bono
                if edad > 60:
                    bonoedad = 30_000
                    total+=bonoedad
                    print(" ")
                    print(f"El valor de subsidio de arriendo es: {total}")
                    break
                else:
                    bonoedad = 0
                    print(" ")
                    print(f"El valor de subsidio de arriendo es: {total}")
                    break
            else:
                subsidio = 300_000    
                total = subsidio+bono 
                if edad > 60:
                    bonoedad = 30_000
                    total+=bonoedad
                    print(" ")
                    print(f"El valor de subsidio de arriendo es: {total}")
                    break
                else:
                    bonoedad = 0
                    print(" ")
                    print(f"El valor de subsidio de arriendo es: {total}")
                    break
        if nivel >=3:
            if cond == 1:
                subsidio = 150_000
                total = subsidio+bono
                if edad > 60:
                    bonoedad = 30_000
                    total+=bonoedad
                    print(" ")
                    print(f"El valor de subsidio de arriendo es: {total}")
                    break
                else:
                    bonoedad = 0
                    print(" ")
                    print(f"El valor de subsidio de arriendo es: {total}")
                    break
            else:
                subsidio = 200_000    
                total = subsidio+bono 
                if edad > 60:
                    bonoedad = 30_000
                    total+=bonoedad
                    print(" ")
                    print(f"El valor de subsidio de arriendo es: {total}")
                    break
                else:
                    bonoedad = 0
                    print(" ")
                    print(f"El valor de subsidio de arriendo es: {total}")
                    break

    else:
        print("por favor, ingrese datos válidos, intentelo nuevamente")

    