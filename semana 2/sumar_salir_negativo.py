suma = 0

while True:
    numero = int(input("ingrese los numeros que desea sumar: "))
    if numero >= 0:
        suma = numero + suma
    else:
        break

print(f"la suma de los numeros ingresados es {suma}")