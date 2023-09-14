class carro:
    Marca: '' #propriedades
    Ano = 0
    Nome = ''
    Cor = ''
    numPortas = 2
    veloMax = 0

#cria um objeto
citroenC3 = carro()
citroenC3.Marca = 'Citroen'
citroenC3.Ano = 2020
citroenC3.Nome = 'Citroen C3'
citroenC3.Cor = 'Branco'
citroenC3.numPortas = 4
citroenC3.veloMax = 173
print('A cor do carro é:',citroenC3.Cor)

#metodo
class carro:
    Nome: ''
    def Ligar(self):
        print('Ligando o', self.Nome)

citroenC3 = carro()
citroenC3.Nome = 'Citroen C3'
citroenC3.Ligar()

#metodo de construção
class carro:
    def __init__(self,nome,cor,ano):
        self.nome = nome
        self.cor = cor
        self.ano = ano
fusca = carro('Fusca', "Azul", 1965)