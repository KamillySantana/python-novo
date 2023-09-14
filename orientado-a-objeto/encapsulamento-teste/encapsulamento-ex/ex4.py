class Livro:
    def __init__(self, titulo, autor, ano, preco_producao):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.__preco_producao = preco_producao

    def o_titulo(self):
        return self.titulo

    def o_autor(self):
        return self.autor

    def o_ano(self):
        return self.ano

    def o_preco_producao(self):
        return self.__preco_producao

    def atualizar_ano(self, novo_ano):
        self.ano = novo_ano

livro = Livro("Dom Casmurro", "Machado de Assis", 1899, 50.00)

print(f"Título: {livro.o_titulo()}")
print(f"Autor: {livro.o_autor()}")
print(f"Ano: {livro.o_ano()}")
print(f"Preço de Produção: {livro.o_preco_producao()}")

novo_ano = int(input("Digite o novo ano do livro: "))
livro.atualizar_ano(novo_ano)

print(f"Novo ano: {livro.o_ano()}")
