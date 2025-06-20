numeros = [int(x) for x in input("Introduce una lista de númerosseparados por espacio: ").split()]
contador_negativos = 0

for numero in numeros:
    if numero < 0:
        contador_negativos += 1

print(f"Hay {contador_negativos} números negativos en la lista.")
