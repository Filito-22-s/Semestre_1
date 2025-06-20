while True:
    try:
        cantidad = int(input("ingrese la cantidad de animales que desea ingresar: "))
        break
    except ValueError:
        print("Debe ingresar numeros enteros")
