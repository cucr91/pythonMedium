import os
from pathlib import Path
import sys


def cli(args):
    if len(args) == 1:
        print("no se pasaron argumentos")
        return
    if len(args) != 3:
        print("se necesitan 2 argumentos")
        return

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("origen no exite")
        return

    destino = args[2]
    d = Path(destino)
    if d.exists():
        print("el destino no puede existir")
        return

    os.rename(str(origen), str(destino))
    print("El archivo renombrado con exito")


cli(sys.argv)
