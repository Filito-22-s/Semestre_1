from funcion_rut import validarRut

rut = input("ingrese su rut, sin puntos y guion y sin el digito verificador: ")

rut = validarRut(rut)
print(f"{rut}")