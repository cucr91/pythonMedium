from pathlib import Path

# Path(r"C\Archivos de programa\Minecraf")  # ruta absoluta para windows
# Path("/usr/bin")  # ruta absoluta para mac y linux
# Path()
# Path.home()
# Path("one/__init__.py")  # ruta relativa para mac y linux

# path = Path("hola-mundo/mi-archivo.py")
# Path.is_file()
# Path.is_dir()
# Path.is_exists()

# print(
#     path.name,
#     path.stem,
#     path.suffix,
#     path.parent,
#     path.absolute()
# )

p = Path.with_name("chanchito.py")
print("p")
p = Path.with_suffix(".bat")
print("p")
p = Path.with_stem("feliz")
print("p")
