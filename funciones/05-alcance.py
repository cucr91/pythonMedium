saludo = "hola global"


def saludar():
    global saludo
    saludo = "hola mundo"


def saludaChanchito():
    saludo = "hola chanchito"
    print(saludo)


print(saludo)

saludar()
print(saludo)
