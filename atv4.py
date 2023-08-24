#Crie uma classe Produto com atributos nome e preco. Crie classes filhas
# como Livro e Eletronico que herdem da classe Produto e adicionem atributos
# específicos, como autor e voltagem.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor

class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem