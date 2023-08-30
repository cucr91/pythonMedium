# duck typing: si esque camina como pato y suena como pato entonces es un pato.-

class Usuario():
    def guardar(self):
        print("Guardando en la base de datos")


class Seccion():
    def guardar(self):
        print("Guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
seccion = Seccion()

guardar([seccion, usuario])
