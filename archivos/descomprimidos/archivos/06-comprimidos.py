from pathlib import Path
from zipfile import ZipFile

# escribir archivos comprimidos
with ZipFile("archivos/comprimidos.zip", "w") as zip:
    # curso pythonmedium
    for path in Path().rglob("*.*"):
        print(path)
        if str(path) != "archivos/comprimidos.zip":
            zip.write(path)


# leer archivos comprimidos
# with ZipFile("archivos/comprimidos.zip") as zip:
#     print(zip.namelist())
