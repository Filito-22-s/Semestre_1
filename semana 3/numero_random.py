from random import randint

while True:
    n1 =int(input("ingrese el primer numero: "))
    if n1 ==0:
        break
    n2=int(input("ingrese el segundo numero: "))
    if n2 <=n1:
        break

    num =randint(n1,n2)
    print(f"el numero random es: {num}")