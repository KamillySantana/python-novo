class Carro:
    def __init__(self,nome,cor,marca):
        self.nome = nome
        self.cor = cor
        self.marca = marca
    def Ligar(self):
        print('Ligando o',self.nome)

class CarroCitroen (Carro):
    def __init__(self,nome,cor,portas):
        super().__init__(nome,cor,'Citroen')
        self.portas = portas
    def Ligar(self):
        print('Ligando 2 o',self.nome)

Car1 = CarroCitroen('C3','Branco')
Car2 = CarroCitroen('Cactus','Azul')
print(Car1.nome, Car1.cor)
print(Car2.nome, Car2.cor)

class Carro2:
    def __init__(self,ano):
        self.ano = ano
        def Farol(self):
            print('Ascendendo as luzes')
        def Acelerar(self):
            print('Acelerando...')

class CarroCiroen (Carro, Carro2):
    def __init__(self,nome,cor,portas,ano):
        Carro.__init__(self,nome,cor,'Citroen')
        Carro2.__init__(self,ano)
        self.portas = portas

Car = CarroCiroen("Cactus","Azul",2,2022)