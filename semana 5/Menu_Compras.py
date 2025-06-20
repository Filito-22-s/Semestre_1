cantidad = 0
credito = -100_000
debito = 250_000
i=0
opsalir = 0
precio = 0
resta = 0
suma = 0

while True:
    print(" \nMenu de opciones de Banco Colipato \n \n1.-Pago De Tarjeta De Credito \n2.-Simulacion De Compras \n3.-Salir  ")
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion >= 1 and opcion <=3:
                break
            else:
                print("Opción no válida, ingrese una opción válida entre 1,2 o 3")
        except ValueError:
            print("Entrada inválida. Ingrese un número (1, 2 o 3).")
    
    match opcion:
        case 1:
            print(f"\nPago De Tarjeta De Credito \n\ntiene ${credito}")

            while True:
                try:
                    monto = int(input("Ingrese el monto que desea pagar: $"))
                    if monto > 0:
                        if monto > debito:
                            print("El monto ingresado supera el saldo actual")
                        else:
                            debito -= monto
                            credito += monto
                            break
                    else:
                        print("Error el monto debe ser mayor a 0")
                except ValueError:
                    print("Entrada inválida. Ingrese un número mayor a cero")

            print(f"\nSu nuevo saldo es de ${credito}")
            print("\n ¿desea salir del programa?\n1.-Si\n2.-No")

            while True:
                try:
                    opsalir = int(input("escribe el numero de tu opcion: "))
                    if opsalir > 0 and opsalir < 3:
                        if opsalir == 1:
                            print("muchas gracias por usar el Banco Colipato")
                            break
                        else:
                            break
                    else:
                        print("ingrese una opción válida entre el 1 y 2")
                except ValueError:
                    print("Entrada inválida. Ingrese la opción 1 o 2")

            if opsalir == 1:
                break
            else:
                seguir = ""

        case 2:
            print("\nSimulacion De Compras\n")
            if credito < 0:
                print("Usted tiene una deuda, no puede realizar ninguna compra")
            else:
                cantidad = int(input("ingrese la cantidad de compras que desea realizar "))

                for i in range (1,cantidad+1):

                    while True:
                        try:
                            precio = int(input(f"ingrese el precio de su {i} producto: $"))
                            if precio >= 0:
                                if precio > credito:
                                    print("El monto de la compra supera el saldo actual de la tarjeta de credito\nIntente nuevamente\n")
                                else:
                                    credito -= precio
                                    suma+=precio
                                    break
                            else:
                                print("ingrese un numero mayor que cero")
                        except ValueError:
                            print("Entrada inválida. Ingrese un número mayor a cero")

                print(f"El precio de la compra es de ${suma} \nSu nuevo saldo es de ${credito} ")
                print("\n ¿desea salir del programa?\n1.-Si\n2.-No")
                precio = 0

                while True:
                    try:
                        opsalir = int(input("escribe el numero de tu opcion: "))
                        if opsalir > 0 and opsalir < 3:
                            if opsalir == 1:
                                print("\nmuchas gracias por usar el Banco Colipato")
                                break
                            else:
                                break
                        else:
                            print("ingrese una opción válida entre el 1 y 2")
                    except ValueError:
                        print("Entrada inválida. Ingrese la opción 1 o 2")

                if opsalir == 1:
                    break
                else:
                    seguir = ""

        case 3:
            print("muchas gracias por usar el Banco Colipato")
            break