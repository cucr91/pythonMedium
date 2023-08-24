punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
# print(punto, punto["lala"])
if "lala" in punto:
    print("encontre a lala", punto["lala"])
else:
    print("no encontre a lala")


print(punto.get("x"))
print(punto.get("lala", 97))

del punto["x"]
del (punto["y"])

print(punto)

punto["x"] = 25
for valor in punto:
    print(valor)

for valor in punto.items():
    print(valor)

# desempaquetado
for llave, valor in punto.items():
    print(llave, valor)


usuarios = [
    {"id": 1, "nombre": "felipe"},
    {"id": 2, "nombre": "camilo"},
    {"id": 3, "nombre": "nicolas"},
    {"id": 4, "nombre": "lorenzo"},
]
for usuario in usuarios:
    print(usuario["nombre"])
