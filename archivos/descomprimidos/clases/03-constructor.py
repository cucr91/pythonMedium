class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: guau!")


mi_perro = Perro("chocolate", 1)
mi_perro.habla()
