puntos = int(input("ingrese la puntuacion del estudiante: "))

if puntos <= 59 :
    print ("su calificacion es una F")
elif puntos >=60 and puntos <= 69:
    print ("su calificacion es una D")
elif puntos >=70 and puntos <= 79:
    print ("su calificacion es una C")
elif puntos >=80 and puntos <= 89:
    print ("su calificacion es una B")
else:
    print ("su calificacion es una A")