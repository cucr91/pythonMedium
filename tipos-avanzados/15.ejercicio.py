from pprint import pprint

# 1- Eliminar los espacios en blanco de un string y devolver una lista con los caracteres restantes.-
# 2- Contar en un diccionario cuanto se repiten los caracteres restantes.-
# 3- Ordenar las llaves de un diccionario por el valor que tienen y devolver el valor en tuplas.
# 4- De un listado de tuplas, devolver las tuplas que contengan el mayor valor.-
# 5- Crea un mensaje que diga:  Los caracteres que mas se repiten son:


string = "hola mundo este es mi string"


def quita_espacio(texto):
    return [char for char in texto if char != " "]


def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True
    )


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def crea_mensaje(diccionario):
    mensaje = "Los caracteres que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones \n"
    return mensaje


sinEspacio = quita_espacio(string)
contados = cuenta_caracteres(sinEspacio)
ordenado = ordena(contados)
mayores = mayores_tuplas(ordenado)
mensaje = crea_mensaje(mayores)
print(mensaje)
