#Crie uma classe Instrumento com um método tocar().
# Crie classes filhas como Violino, Piano e Flauta que herdem da classe
# Instrumento e sobrescrevam o método tocar().

class Instrumento:
    def tocar(self):
        pass

class Violino(Instrumento):
    def tocar(self):
        return "Tocando o violino"

class Piano(Instrumento):
    def tocar(self):
        return "Tocando o piano"

class Flauta(Instrumento):
    def tocar(self):
        return "Tocando a flauta"