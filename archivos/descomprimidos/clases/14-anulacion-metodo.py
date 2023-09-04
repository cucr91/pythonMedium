class ave():
    def __init__(self):
        self.volador = True

    def vuela(self):
        print("vuela ave")


class pato(ave):
    def __init__(self):
        super().__init__()
        self.nada = True

    def vuela(self):
        print("vuela pato")


pato = pato()
pato.vuela()
print(pato.volador, pato.nada)
