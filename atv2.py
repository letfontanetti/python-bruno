#Crie uma classe Animal com um método fazer_som(). Em seguida,
# crie classes filhas como Cachorro, Gato e Vaca que sobrescrevam o método fazer_som().

class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "auauuuu"

class Gato(Animal):
    def fazer_som(self):
        return "miauuuu"

class Vaca(Animal):
    def fazer_som(self):
        return "Muuuuuuuu"