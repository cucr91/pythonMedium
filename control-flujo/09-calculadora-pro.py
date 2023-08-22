bienvenida = "Bienvenido a la calculadora ultimatum 2030"
salir = "Para salir, escriba \"salir\""
operaciones = "Las operaciones son: suma, resta, multiplicación, división.  Exito en tus calculos "
print(bienvenida)
print(salir)
print(operaciones)

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingrese operación: ")
    if op.lower() == "salir":
        break
    n2 = input("ingrese el siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operacion incorrecta, vuelva a intentar. ")
        break

    print(f"el resultado es {resultado}")


# n1 = input("Ingresa el primer numero: ")
# op = input("ingrese operación: ")
# n2 = input("Ingresa el segundo numero: ")
# n1 = int(n1)
# n2 = int(n2)
# suma = n1 + n2
# resta = n1 - n2
# multi = n1 * n2
# divi = n1 / n2

# for op in operaciones:
#     if op == "suma":
#         print(suma)
#         break
#     elif op == "resta":
#         print(n1 - n2)
#         break
#     elif op == "multi":
#         print(n1 * n2)
#         break
#     elif op == "divi":
#         print(n1 / n2)
#         break
#     else:
#         print("operacion NO encontrada, vuelve a ingresar")


# mensaje = f"""
# Para los numeros {n1} y {n2},
# el resultado de la suma es {suma}
# el resultado de la resta es {resta}
# el resultado de la multiplicación es {multi}
# el resultado de la división es {divi}
# """
# print(mensaje)
