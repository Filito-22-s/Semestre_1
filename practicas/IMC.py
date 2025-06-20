
while True:
    peso = float(input("ingrese su peso en KILOS: "))
    altura = float(input("ingrese su altura METROS: "))
    edad = int(input("ingrese su edad: "))
    if peso > 0 and altura > 0 and edad > 0:

        imc = peso / altura
        print(f"{imc}")

        if imc < 22.0 and edad < 45:
            print("su condicion de riesgo es baja")
            break

        elif imc < 22.0 and edad >=45:
            print("su condicion de riesgo es meida")
            break

        elif imc >= 22.0 and edad < 45:
            print("su condicion de riesgo es media")
            break

        elif imc >= 22.0 and edad >= 45:
            print("su condicion de riesgo es alta")
            break
    else:
        print("los datos ingresados deben ser positivos")