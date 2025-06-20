def sacar_puntaje(porcentaje, puntaje):
    return (porcentaje * puntaje)/100

def nota_presentacion(nota_1,nota_2,nota_3):
    return nota_1 + nota_2 + nota_3

def nota_final(nota_presentacion,nota_examen):
    return ((nota_presentacion * 60)/100) + ((nota_examen * 40)/100)

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

while True:
    not1 = float(input("ingrese su primera nota: "))
    not2 = float(input("ingrese su segunda nota: "))
    not3 = float(input("ingrese su tercera nota: "))

    resultado_1 = sacar_puntaje(not1,33)
    resultado_2 = sacar_puntaje(not2,33)
    resultado_3 = sacar_puntaje(not3,34)

    nota_p = nota_presentacion(resultado_1, resultado_2, resultado_3)

    print(f"su nota de precentacion es {nota_p}")

    examen = float(input("ingrese su nota de examen: "))
    nota_f = nota_final(nota_p, examen)
    print (f"\nsu nota Final es {nota_f}\n")
    
    if not menu_salida():
        break