class Instrumento:
    def tocar(self):
        print('Tocando')

class Violino(Instrumento):
    def tocar(self):
        print('Tocando o violino')

class Piano(Instrumento):
    def tocar(self):
        print('Tocando o piano')

class Flauta(Instrumento):
    def tocar(self):
        print('Tocando a flauta')

# Testando as classes
violino = Violino()
piano = Piano()
flauta = Flauta()

violino.tocar()
piano.tocar()
flauta.tocar()


