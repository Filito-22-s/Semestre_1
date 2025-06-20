invitados = int(input("ingrese la cantidad de invitados: "))
p1 = 10_000
p2 = 8_500
p3 = 7_500
total = 0


if invitados < 200 and invitados >0:
    total = p1 * invitados
    print(f"el precio total es {total} ")
elif invitados >=200 and invitados < 300:
    total = p2 *invitados
    print(f"el precio total es {total} ")
elif invitados >=300 :
    total = p3 * invitados
    print(f"el precio total es {total} ")
else:
    print("error")