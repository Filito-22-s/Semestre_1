cheetos = 800    
monster = 1200    
gretel = 950
precio = 0 


while True:

    print("Maquina expendedora")
    print("-------------------")
    print("A.- Cheetos")
    print("B.- Monster")
    print("C.- Gretel")
    print("D.- Salir")

    opcion = (input("ingrese una de las opciones: ")).upper()
    if opcion == "A":
        print("Cheetos $800")
        cant =int(input("ingrese la cantidad que desea: "))
        if cant > 0:
            precio = cheetos * cant
            print(f"debe pagar {precio}")
        else:
            print("cantidad debe ser mayor a 0")

    elif opcion == "B":
        print("Monster $1200")
        cant =int(input("ingrese la cantidad que desea: "))
        if cant > 0:
            precio = monster * cant
            print(f"debe pagar {precio}")
        else:
            print("cantidad debe ser mayor a 0")

    elif opcion == "C":
        print("Gretel $950")
        cant =int(input("ingrese la cantidad que desea: "))
        if cant > 0:
            precio = gretel * cant
            print(f"debe pagar {precio}")
        else:
            print("cantidad debe ser mayor a 0")  

    elif opcion == "D":
        print ("muchas gracias por usar la maquina expendedora")
        break
    else:
        print("opcion invalida. por favor, ingresa una opcion válida")