#Crie uma classe Bebida com atributos nome e tipo.
# Crie classes filhas como Refrigerante e Cafe que herdem da classe Bebida
# e adicionem atributos específicos

class Bebida:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

class Refrigerante(Bebida):
    def __init__(self, nome, tipo, sabor):
        super().__init__(nome, tipo)
        self.sabor = sabor

class Cafe(Bebida):
    def __init__(self, nome, tipo, intensidade):
        super().__init__(nome, tipo)
        self.intensidade = intensidade