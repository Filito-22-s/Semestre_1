def mostrar_menu():
    print("1.- Continuar")
    print("2.- Salir")

def menu_salida():
    while True:
        try:
            mostrar_menu()
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    print("Has seleccionado continuar.\n")
                    return True
                case 2:
                    print("Saliendo del programa.")
                    return False
                case _:
                    print("Opción inválida.")
        except ValueError:
            print("Ingrese una opción válida (1 o 2)")