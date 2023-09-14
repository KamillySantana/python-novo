class Animal:
    def fazer_som(self):
        print('Animal som')

class Cachorro(Animal):
    def fazer_som(self):
        print('Cachorro faz: Au au!')

class Gato(Animal):
    def fazer_som(self):
        print('Gato faz: Miau!')

class Vaca(Animal):
    def fazer_som(self):
        print('Vaca faz: Muuuuu!')

cachorro = Cachorro()
gato = Gato()
vaca = Vaca()

cachorro.fazer_som()
gato.fazer_som()
vaca.fazer_som()
