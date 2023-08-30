from abc import ABC, abstractclassmethod


class Model(ABC):
    @property
    @abstractclassmethod
    def tabla():
        pass

    @abstractclassmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("guardando usuario")


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)
