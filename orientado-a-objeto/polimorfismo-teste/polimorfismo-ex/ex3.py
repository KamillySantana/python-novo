class Calculo:
    def calcular(self, num, num2):
        pass

class Soma(Calculo):
    def calcular(self, num, num2):
        return num + num2

class Subtracao(Calculo):
    def calcular(self, num, num2):
        return num - num2

class Multiplicacao(Calculo):
    def calcular(self, num, num2):
        return num * num2

class Divisao(Calculo):
    def calcular(self, num, num2):
        return num / num2

soma = Soma()
subtracao = Subtracao()
multiplicacao = Multiplicacao()
divisao = Divisao()

num1 = float(input("Digite um número: "))
num2 = float(input("Digite o segundo número: "))

print(f"Soma: {soma.calcular(num1, num2)}")
print(f"Subtração: {subtracao.calcular(num1, num2)}")
print(f"Multiplicação: {multiplicacao.calcular(num1, num2)}")
print(f"Divisão: {divisao.calcular(num1, num2)}")






