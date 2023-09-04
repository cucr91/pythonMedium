class producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"


class Categoria:
    producto = []

    def __init__(self,  nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


kayak = producto("kayak", 1000)
bicicleta = producto("bicicleta", 750)
surfboard = producto("surfboard", 500)
deportes = Categoria("Deportes", [kayak, bicicleta])
deportes.agregar(surfboard)
deportes.imprimir()
