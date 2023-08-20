animal = "  Perro ChoColaTe  "
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())
print(animal.title())
print(animal.strip())
print(animal.lstrip())
print(animal.rstrip())
print(animal.find("rr"))
print(animal.replace("ChoColaTe", "chocolo"))

# siguientes metodos devuelven un bolean
print("ChoColaTe" in animal)
print("ChoColaTe" not in animal)
