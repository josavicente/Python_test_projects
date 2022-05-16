def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooom")
    print(f"Fin de la función: {num}")

cuenta_atras(10)


def factorial(num):
    print(f"Valor inicial -> {num}")
    if num > 1:
        num = num * factorial(num - 1)
    print(f"Valor final -> {num}")
    return num

print(factorial(5))