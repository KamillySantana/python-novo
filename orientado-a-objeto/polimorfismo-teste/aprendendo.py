#pega um metodo alterar esse metodo e sobrescrever ele

#classe pai
# metodos dinamicos (funcionalidades)
#classe filho 1 e 2
# sobrescritos e alterados (funcionalidades)

class Profissao:
    def Acao(self):
        pass

class estudante(Profissao):
    def Acao(self):
        print('Estudando...')

aluno1 = estudante()
aluno1.Acao()

#outra forma sem a a palavra pass

class profissao:
    def Acao(self):
        return 'A principal atividade é:'
class Estudante(profissao):
    def Acao(self):
        print(super().Acao(),'Estudar')