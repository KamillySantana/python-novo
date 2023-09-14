class Forma:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

class Retangulo(Forma):
    def calcular_area(self):
        return self.largura * self.altura

class Triangulo(Forma):
    def calcular_area(self):
        return (self.largura * self.altura) / 2

retangulo = Retangulo(5, 3)
triangulo = Triangulo(4, 6)

area_retangulo = retangulo.calcular_area()
area_triangulo = triangulo.calcular_area()

print("Área do retângulo:", area_retangulo)
print("Área do triângulo:", area_triangulo)
