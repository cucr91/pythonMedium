nombre = "Camilo"
apellido = "Calderon"
# Manera poco elegante"
# nombre_completo = nombre + " " + apellido
nombre_completo = f"{nombre} {apellido}"
nombre_completo = f"{nombre[0]} {apellido[0]}"
print(nombre_completo)
