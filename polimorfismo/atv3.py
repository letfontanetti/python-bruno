class calculo:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

        def calcular(self):
            pass


class soma(calculo):
    def __init__(self,num1,num2):
        super().__init__(num1,num2)

    def calcular(self):
        return self.num1 + self.num2

class subtracao(calculo):
    def __init__(self,num1,num2):
        super().__init__(num1,num2)

    def calcular(self):
        return self.num1 - self.num2

class multiplicacao(calculo):
    def __init__(self,num1,num2):
        super().__init__(num1,num2)

    def calcular(self):
        return self.num1 * self.num2
