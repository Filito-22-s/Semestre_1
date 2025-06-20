colores = ["rojo","azul","verde","naranjo"]

colores.append("negro") #agregar un elemento al array
colores.insert(1,"morado") #agregar un elemento al arrayd en la posicion escojida /en este caso 1
colores.remove("rojo") #borrar una de las variables del arreglo

print(colores[2])

for color in colores:
    print(f"el color es: {color}")