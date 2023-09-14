class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_valor(self):
        return self.preco

class Produto(Item):
    def __init__(self, nome, preco, quantidade):
        super().__init__(nome, preco)
        self.quantidade = quantidade

    def calcular_valor(self):
        return self.preco * self.quantidade


class Servico(Item):
    def __init__(self, nome, preco, horas):
        super().__init__(nome, preco)
        self.horas = horas

    def calcular_valor(self):
        return self.preco * self.horas

produto = Produto("Camiseta", 20, 3)
servico = Servico("Consultoria", 50, 2)

print(f"Valor do produto: R${produto.calcular_valor()}")
print(f"Valor do serviço: R${servico.calcular_valor()}")
