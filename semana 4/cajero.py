saldo = 100_000

while True:
    print ("bienvenido al banco del pais, seleccione una opcion")
    print ("1. consultar saldo")
    print ("2. retirar dinero")
    print ("3. depositar dinero")
    print ("4. salir")

    opcion =int(input("Seleccione una opcion (1-4): "))

    if opcion == 1:
        print (f"tu saldo actual es {saldo} ")

    elif opcion == 2:
        cantidad_retiro = int(input("ingrese la cantidad de dinero que desea retirar : $"))
        if cantidad_retiro <= saldo:
            saldo -= cantidad_retiro
            print (f"has retirado ${cantidad_retiro}. Nuevo saldo: ${saldo}")

        else:
            print("saldo insuficiente, No es posible realizar el retiro.")

    elif opcion == 3:
        deposito = int(input("ingrese la cantidad de dinero que desea depositar : $"))
        saldo += deposito
        print(f"usted a depositado ${deposito}. nuevo saldo es ${saldo} ")

    elif opcion == 4:
        print ("gracias por utilizar el cajero")
        break

    else:
        print("opción inválida. por favor, ingrese una opcion válida ")
