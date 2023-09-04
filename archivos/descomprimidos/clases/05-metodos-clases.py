class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("guau!")

    @classmethod
    def factory(cls):
        return cls("chanchito feliz", 4)


Perro.habla()
Perro1 = Perro("chanchito", 2)
Perro2 = Perro("Felipe", 3)
Perro3 = Perro.factory()
print(Perro3.edad, Perro3.nombre)
