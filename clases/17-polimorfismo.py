from abc import ABC, abstractclassmethod


class Model(ABC):
    @abstractclassmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print("Guardando en la base de datos")


class Seccion(Model):
    def guardar(self):
        print("Guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
seccion = Seccion()

guardar([seccion, usuario])
