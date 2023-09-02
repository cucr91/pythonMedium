from pathlib import Path
import db
import api
import graphql

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": db,
    "api": api,
    "graphql": graphql
}


def load(p):
  #  print()
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene funcion init")


list(map(load, paths))
