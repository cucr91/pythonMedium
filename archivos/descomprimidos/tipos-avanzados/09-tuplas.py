numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto)

for n in numeros:
    print(n)

# creamos lista en base a la tupla, para modificar la lista
listaNumeros = list(numeros)
listaNumeros[0] = "chanchito feliz"
print(listaNumeros)
