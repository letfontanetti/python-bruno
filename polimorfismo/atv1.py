class animalaquatico:
    def nadando(self):
        pass

class peixe(animalaquatico):
    def nadando(self):
        print('peixinho glubglub...')

class tartaruga(animalaquatico):
    def nadando(self):
        print('tartaruguinha nhacnhac...')

peixinho = peixe()
peixinho.nadando()

tartaruguinha = tartaruga()
tartaruguinha.nadando()