class profissao:
    def acao(self):
        return 'a principal atividade é:'
class estudante(profissao):
    def acao(self):
        print(super().acao(), 'estudar')

leleti = estudante()
leleti.acao()
