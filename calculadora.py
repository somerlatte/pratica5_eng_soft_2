class Calculadora:
    def __init__(self):
        pass

    def adicao(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Erro: não é possível dividir por zero"
