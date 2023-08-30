class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Clase perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: guau ")


perro = Perro("chocolate", 5)
print(perro)
texto = str(perro)
print(texto)
