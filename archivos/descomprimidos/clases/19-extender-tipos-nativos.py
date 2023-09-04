# lista = list([1, 2, 3])
# lista.append(4)
# lista.insert(0, 0)
# print(lista)

# existe una mejor manera de poder crear metodos para estos tipos para que nuestro codigo sea mas intuitivo.-


class Lista(list):
    def prepend(self, item):
        self.insert(0, item)


lista = Lista([1, 2, 3])
lista.append(4)
lista.insert(0, 0)
print(lista)
