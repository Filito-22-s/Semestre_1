for i in range (1,30):
    if i % 5 == 0 and i % 3 == 0:
        print(f"el numero {i} es un multiplo de 3 y 5")
    elif i % 3 == 0:
        print(f"el numero {i} es un multiplo de 3")
    elif i % 5 == 0:
        print(f"el numero {i} es un multiplo de 5")
    else:
        print(f"{i} es otro numero")
    