class Model():
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, Definir tabla")

    def guardar(self):
        print(F"Guardando {self.tabla} en Base de datos")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)
