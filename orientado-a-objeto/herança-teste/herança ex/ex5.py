class Veiculo:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Carro(Veiculo):
    def __init__(self,marca,modelo,ano,portas):
        super().__init__(marca,modelo,ano)
        self.portas = portas

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, marcha):
        super().__init__(marca, modelo, ano)
        self.marcha = marcha

carro = Carro("Toyota", "Corolla", 2022, 5)
moto = Moto("Honda", "GC 160 Fan", 2015, 'Tem marcha')

print("Carro:", carro.marca, carro.modelo, carro.ano, carro.portas)
print("Moto:", moto.marca, moto.modelo, moto.ano, moto.marcha)
