#Crie uma classe Veiculo com atributos marca, modelo e ano.
# Crie classes filhas como Carro e Moto que herdem da classe Veiculo e
# adicionem atributos específicos.

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas