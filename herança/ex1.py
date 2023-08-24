class carro:
    def __init__(self,nome,cor,marca):
        self.nome = nome
        self.cor = cor
        self.marca = marca
    def Ligar(self):
        print('ligando', self.nome)

class carro2:
    def __init__(self,ano):
        self.ano = ano
    def farol(self):
        print('acendendo as luzes')
    def acelerar(self):
        print('acelerando...')

class carrocitroen(carro, carro2):
    def __init__(self,nome,cor,portas,ano):
        super().__init__(nome,cor,"citroen")
        carro.__init__(self,nome,cor, 'citroen')
        carro2.__init__(self,ano)
        self.portas = portas

car1 = carrocitroen('c3', 'branco', 4, 2022)
car2 = carrocitroen('cactus', 'azul', 2, 2023)
print(car1.nome, car1.cor, car1.marca, car1.portas, car1.ano)
print(car2.nome, car2.cor, car2.marca, car2.portas, car2.ano)