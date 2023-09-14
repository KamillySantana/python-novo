class AnimalAquatico:
    def nadando(self):
        pass

class Peixe(AnimalAquatico):
    def nadando(self):
        print('glub glub...')

class Tartaruga(AnimalAquatico):
    def nadando(self):
        print('Nadando......')

peixe = Peixe()
peixe.nadando()

tartaruga = Tartaruga()
tartaruga.nadando()