def limpiar_decimales(porcentaje):
    if porcentaje == "1" or porcentaje == "2" or porcentaje == "3" or porcentaje == "4" or porcentaje == "5" or porcentaje == "6" or porcentaje == "7" or porcentaje == "8" or porcentaje == "9":
        porcentaje = "0.0" + porcentaje
        porcentaje = float(porcentaje)
        return porcentaje
    else:
        porcentaje = "0." + porcentaje
        porcentaje = float(porcentaje)
        return porcentaje

n1 = input("ingrese un porcentaje: ")
resultado = limpiar_decimales(n1)

print(f"su porcentaje es de {resultado}")