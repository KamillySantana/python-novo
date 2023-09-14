class Cilente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.__telefone = telefone

    def mostrar(self):
        print(self.__telefone)

a = Cilente('Bruno', 1899765437)
a.mostrar()