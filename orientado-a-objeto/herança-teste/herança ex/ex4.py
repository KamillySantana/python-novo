class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

class Livro(Produto):
    def __init__(self,nome,preco,autor):
        super().__init__(nome,preco)
        self.autor = autor

class Eletronicos(Produto):
    def __init__(self,nome,preco,voltagem):
        super().__init__(nome,preco)
        self.voltagem = voltagem

livro = Livro('A escolha', 50, 'Nicholas Sparks')
print(livro.autor, livro.nome, livro.preco)
