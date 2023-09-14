class Carro:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def marca(self):
        return self.__marca

    def modelo(self):
        return self.__modelo

    def novo_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

carro = Carro("Toyota", "Corolla")

print(f"Marca: {carro.marca()}")
print(f"Modelo: {carro.modelo()}")

novo_modelo = input("Digite o novo modelo do carro: ")
carro.novo_modelo(novo_modelo)

print(f"Novo modelo: {carro.novo_modelo()}")
