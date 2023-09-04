from io import open

# escritura
# texto = "hola mundi"

# archivo = open("archivos/hola-mundo.txt", "w")
# archivo.write(texto)
# archivo.close()


# lectura
# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)


# lectura como lista
# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)


# with open("archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())
#     archivo.seek()
#     for linea in archivo:
#         print(linea)


# agregar
# archivo = open("archivos/hola-mundo.txt", "a+")
# archivo.write("chao mundo")
# archivo.close()


#lectura y escritura
with open("archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0]= "chachito feliz"
    archivo.writelines(texto)