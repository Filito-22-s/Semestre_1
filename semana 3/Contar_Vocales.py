palabra = input("Ingrese una palabra: ")
vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
consonantes = "qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM"

vocal_es = []
conso_es = []

cantvocal = 0
cantcons = 0
espacio = 0

for letra in palabra:
        if letra in vocales:
            vocal_es.append(letra)
            cantvocal = cantvocal + 1

        elif letra in consonantes:
            conso_es.append(letra)
            cantcons = cantcons + 1

        else:
            espacio = espacio + 1 

print(f"Las vocales encontradas son: {vocal_es}")
print(f"Las consonantes encontradas son: {conso_es}")

print(f"La cantidad de vocales es: {cantvocal}")
print(f"La cantidad de vocales es: {cantcons}")
print(f"Cantidad de espacios vacios: {espacio} ")