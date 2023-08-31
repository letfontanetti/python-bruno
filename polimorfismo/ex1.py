class profissao:
    def acao(self):
        pass
class estudante(profissao):
    def acao(self):
       print('estudando...')

leleti = estudante()
leleti.acao()