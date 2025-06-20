suma = 0
prom = 0

for i in range (1,6):
    temperatura = float(input(f"la temperatura del dia {i} es: "))
    suma += temperatura
    prom += 1

promedio = suma / prom
print(f"el promedio de las temperaturas es {promedio}")
if promedio < 10:
    print("temperaturas bajas")
elif promedio >= 10 and promedio < 20:
    print("temperaturas medias")
else:
    print("temperaturas altas")
