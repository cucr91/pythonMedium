# lista1 = [1, 2, 3, 4, 5]
# # print(*lista)

# lista2 = [5, 6]

# combinada = ["hola mundo", *lista1, "mundo", *lista2]
# print(combinada)

# tambien podemos utilizar con los diccionarios con 2 asteriscos

punto1 = {"x": 1, "y": "hola"}
punto2 = {"y": 2}

nuevoPunto = {**punto1, "lala": "hola mundo", ** punto2, "z": "mundo"}
print(nuevoPunto)
