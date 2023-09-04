import json
from pathlib import Path

# escribir json
# productos = [
#     {"id": 1, "name": "surfboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "Skate"},
# ]

# data = json.dumps(productos)

# Path("archivos/productos.json").write_text(data)


# leer json
data = Path("archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)
# print(productos)


# modificar json
productos[0]["name"] = "chanchito feliz"
Path("archivos/productos.json").write_text(json.dumps(productos))
