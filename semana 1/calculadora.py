def calcular(numero1, numero2, opcion):
    if opcion == 1:
        return numero1 + numero2
    elif opcion == 2:
        return numero1 - numero2
    elif opcion == 3:
        return numero1 * numero2
    elif opcion == 4:
        return numero1 / numero2
    else:
        return "Opción no válida"
    
def simbolo(opcion):
    if opcion == 1:
        return "+"
    elif opcion == 2:
        return "-"
    elif opcion == 3:
        return "x"
    elif opcion == 4:
        return ":"
    else:
        return ""


print("Calculadora")
print("-------------")
print("1.Sumar")
print("2.restar")
print("3.Mulpuplicar")
print("4.Dividir")
print("para salir dijite cualquier otro numero")

numero1 = 0
numero2 = 0
resultado = 0
opcion = int(input("ingrese una opcion: ")) 
operacion = ""

while opcion > 0 and opcion < 5:

    numero1 = int(input ("ingrese el primer numero de la operacion: "))

    if opcion == 4:

            while True:

                numero2 = int(input ("ingrese el segundo numero de la operacion: "))
                if numero2 == 0:

                    print("error no se puede dividir por 0 ")

                else:

                    break
        
    else:
        numero2 = int(input ("ingrese el segundo numero de la operacion: "))

    operacion = simbolo(opcion)
    resultado = calcular(numero1, numero2, opcion)
    print (f"el resultado de {numero1} {operacion} {numero2} = {resultado}")
    opcion = int(input("ingrese otra opcion: "))
     


print("ha salido del programa")