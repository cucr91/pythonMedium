def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(1, 2, 3)
suma(2, 5)
suma(2, 5, 7, 1, 3)
