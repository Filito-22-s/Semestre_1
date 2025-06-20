from random import randint

num1=int(input("ingrese el numero en el que quiere comenzar: "))
while True:
    num2=int(input("ingrese el limite del rango: "))
    if num2 > num1:
        break
    else:
        print("el limite debe ser mayor al numero de entrada")

numero = randint(num1, num2)
print("                              ")
print(f"intenta adivinar el numero secreto entre {num1} y {num2}, en 3 intentos")

for i in range(1,4):
    print("-----------------------------")
    print(f"intento {i}")
    intento =int(input(f"ingresa un numero entre {num1} y {num2}: "))
    if intento == numero:
        print("                ")
        print("FELICIDADES HAZ GANADO!!!!!")
        break
    else:
        if i == 1:
            if intento > numero:
                print("        ")
                print("este no es el numero secreto :c")
                print(f"el numero es meno que {intento}")
            else:
                print("        ")
                print("este no es el numero secreto :c")
                print(f"el numero es mayor que {intento}")
        elif i == 2:
            if intento > numero:
                print("        ")
                print("este no es el numero secreto :c")
                print(f"el numero es meno que {intento}")
                print("te dare una pista")
                resta=numero - 2
                suma = numero + 4 
                if resta < num1:
                    resta == num1
                else:
                    break
                if suma > num2:
                    suma = num2
                else:
                    break
                print(f"el numero esta mas cerca del {resta} que del {suma} ")

            else:
                print("        ")
                print("este no es el numero secreto :c")
                print(f"el numero es mayor que {intento}")
                print("te dare una pista")
                resta=numero - 2
                suma = numero + 4
                if resta < num1:
                    resta == num1
                else:
                    resta=numero - 2
                    
                if suma > num2:
                    suma = num2
                else:
                    suma = numero + 4
            
                print(f"el numero esta mas cerca del {resta} que del {suma} ")

        elif i==3: 
            print("        ")   
            print("gastaste todos los intentos :´( , mas suerte para la proxima ;)")
    

