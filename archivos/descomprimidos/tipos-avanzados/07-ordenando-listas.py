numeros = [2, 3, 5, 8, 9, 1, 2, 10]
# numeros.sort()
# numeros.sort(reverse=True)
numeros2 = sorted(numeros)
print(numeros)
print(numeros2)


usuarios = [["chanchito", 4], ["felipe", 1], ["pulga", 5]]

usuarios.sort(key=lambda el: el[1])
print(usuarios)
