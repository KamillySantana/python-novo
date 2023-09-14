class Conta:
    def __init__(self, saldo, titular):
        self.__saldo = saldo
        self.titular = titular

    def depositar(self, deposito):
        self.__saldo += deposito

    def sacar(self, retirar):
        self.__saldo -= retirar

    def exibir(self):
        print(self.__saldo)

a = Conta(3000,"Igor")
a.depositar(200)
a.exibir()

a.sacar(400)
a.exibir()