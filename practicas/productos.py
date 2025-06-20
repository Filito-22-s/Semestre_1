suma = 0
promedio = 0
a = 0
b = 0
c = 0
d = 0

for i in range (1,6):
    print("A.- Zapatos")
    print("B.- Poleras")
    print("C.- Pantalón")
    print("D.- Salir")

    opcion =(input("ingrese una opcion: ")).upper()

    if opcion == "A":
        print ("usted compro unos Zapatos: ")
        while True:
            estrella = int(input("califique como fue su experiencia de 1-5: "))
            if estrella <=5 and estrella >=1:
                suma += estrella
                promedio += 1
                a += 1
                break
            else:
                print("ingrese una calificacion entre 1-5")

    elif opcion == "B":
        print ("usted compro una Polera: ")
        while True:
            estrella = int(input("califique como fue su experiencia de 1-5: "))
            if estrella <=5 and estrella >=1:
                suma += estrella
                promedio += 1
                b += 1
                break
            else:
                print("ingrese una calificacion entre 1-5")

    elif opcion == "C":
        print ("usted compro un Pantalon: ")
        while True:
            estrella = int(input("califique como fue su experiencia de 1-5: "))
            if estrella <=5 and estrella >=1:
                suma += estrella
                promedio += 1
                c += 1
            else:
                print("ingrese una calificacion entre 1-5")

    elif opcion == "D":
        print("muchas gracias por visitar nuestra tienda")
        d += 1
    
    else:
        print("EROOR")

if promedio > 0:
    promedio = suma / promedio
    print(f"el promedio de experiencia de compra entre las personas fue de {promedio}")
else: 
    print("no hubo calificaciones")

print(f"{a} personas compraron Zapatos")
print(f"{b} personas compraron Poleras")
print(f"{c} personas compraron Pantalones")
print(f"{d} personas no compraron")