fibonacci = 0
calculo = 0

while True:
    try:
        print("Quieres usar la calculadora de fibonacci")
        print("1 Si")
        print("2 No")
        print("!advertencia se responde con los numeros¡")
        uso = int(input("Responda: "))
        match uso:
            case 1:
                while True:
                    try:
                        cantidad = int(input("Indique la cantidad de veces que se calcule los numeros de Fibonacci: "))
                        cantidad = cantidad + 1
                        for i in range(0,cantidad):
                            calculo = fibonacci + 1
                            resultado = fibonacci + calculo
                            fibonacci = resultado 
                            print(f"El resultado del calculo es: {resultado}")
                        break
                    except ValueError:
                        print("\nOe solo numeros\n")
            case 2:
                print("\nMuchas gracias por usar la calculadora\n")
                break
                #sys.exit
            case _:
                print("Aver cara de monda tienes 2 elecciones que haces eligiendo otra cosa")
    except ValueError:
        print("\nOe solo numeros\n")