#Crie uma classe Forma com atributos largura e altura.
# Crie classes filhas como Retangulo e Triangulo que herdem da classe
# Forma e adicionem métodos para calcular a área.

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