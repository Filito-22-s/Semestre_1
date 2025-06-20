numero = int(input("ingrese el numero de la tabla que desea generar: "))
fintabla = int(input("ingrese hasta que numero quiere que se genere la tabla: "))

for i in range(0,fintabla+1):
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")