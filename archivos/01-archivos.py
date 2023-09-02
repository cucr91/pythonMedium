from pathlib import Path
from time import ctime

archivo = Path("archivos/archivo-prueba.txt")
# archivo.exists()
# archivo.exists()
# archivo.exists()

# print(archivo.stat())


print("acceso", ctime(archivo.stat().st_atime))
print("creacción", ctime(archivo.stat().st_ctime))
print("modificación", ctime(archivo.stat().st_mtime))
# timestamp fecha que tiene un archivo con respecto al 1/1/1970  es una fecha unix.-
