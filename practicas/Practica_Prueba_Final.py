pokemones = {}

tipos_validos = ["fuego", "agua", "hierba", "veneno", "psiquico", "luchador", "eléctrico"]

def mostrar_menu():
    print("\nMENÚ PRINCIPAL")
    print("1.- Ingresar pokemon")
    print("2.- Buscar pokemon")
    print("3.- Eliminar pokemon")
    print("4.- Listar pokemones")
    print("5.- Salir")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    ingresar_pokemon()
                case 2:
                    buscar_pokemon()
                case 3:
                    eliminar_pokemon()
                case 4:
                    listar_pokemones()
                case 5:
                    print("¡Hasta luego!")
                    break
                case _:
                    print("Debe seleccionar una opción válida.")
        except ValueError:
            print("ingrese la opcion como valor numerico")

def ingresar_pokemon():
    while True:
        try:
            id = int(input("Ingrese ID del pokemon: "))
            if id > 0:
                break
            else:
                print("ingrese solo numeros positivos")
        except ValueError:
            print("ingrese solo valores numericos")
        
    try:
        nombre = input("Ingrese nombre del pokemon: ").lower()
        if nombre in pokemones:
            print("El nombre del pokemon ya existe.")
            return

        tipo = input(f"Ingrese tipo del pokemon {tipos_validos}: ").lower()
        if tipo not in tipos_validos:
            print("Tipo de pokemon inválido.")
            return

        codigo = input("Ingrese código del pokemon: ")
        if not validar_codigo(codigo):
            print("Código inválido. Debe tener mínimo 8 caracteres, incluir al menos una letra, un número y no tener espacios.")
            return

        pokemones[nombre] = {
            "id": id,
            "nombre": nombre,
            "codigo": codigo,
            "tipo": tipo
        }
        print("¡Pokemon ingresado exitosamente!")
    except Exception as e:
        print(f"Error al ingresar el pokemon: {e}")

def validar_codigo(codigo):
    if len(codigo) < 8:
        return False
    if ' ' in codigo:
        return False
    if not any(char.isdigit() for char in codigo):
        return False
    if not any(char.isalpha() for char in codigo):
        return False
    return True

def buscar_pokemon():
    nombre = input("Ingrese el nombre del pokemon a buscar: ").lower()
    if nombre in pokemones:
        pokemon = pokemones[nombre]
        print(f"Nombre: {pokemon['nombre']}")
        print(f"Tipo: {pokemon['tipo']}")
        print(f"Código: {pokemon['codigo']}")
    else:
        print("El pokemon no se encuentra.")

def eliminar_pokemon():
    nombre = input("Ingrese el nombre del pokemon a eliminar: ").lower()
    if nombre in pokemones:
        del pokemones[nombre]
        print("¡Pokemon eliminado!")
    else:
        print("¡No se pudo eliminar pokemon!")

def listar_pokemones():
    if not pokemones:
        print("No hay pokemones registrados.")
    else:
        for pokemon in pokemones.values():
            print(f"ID: {pokemon['id']}, Nombre: {pokemon['nombre']}, Tipo: {pokemon['tipo']}")

main()