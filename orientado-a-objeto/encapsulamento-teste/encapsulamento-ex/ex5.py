class Restaurante:
    def __init__(self, nome, tipo, gasto_mensal):
        self.nome = nome
        self.tipo = tipo
        self.__gasto_mensal = gasto_mensal

    def nome_res(self):
        return self.nome

    def tipo_res(self):
        return self.tipo

    def gasto_mensal(self):
        return self.__gasto_mensal

    def mudar_tipo(self, novo_tipo):
        self.tipo = novo_tipo


# Exemplo de uso
restaurante = Restaurante("Casa Italiana", "Italiano", 5000.00)

print(f"Nome: {restaurante.nome_res()}")
print(f"Tipo: {restaurante.tipo_res()}")
print(f"Gasto Mensal: {restaurante.gasto_mensal()}")

novo_tipo = input("Digite o novo tipo do restaurante: ")
restaurante.mudar_tipo(novo_tipo)

print(f"Novo tipo: {restaurante.tipo_res()}")
