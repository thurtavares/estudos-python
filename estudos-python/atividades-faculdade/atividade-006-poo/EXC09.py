from abc import ABC, abstractmethod


class EstrategiaFrete(ABC):

    @abstractmethod
    def calcular(self, peso, distancia):
        pass


class Sedex(EstrategiaFrete):

    def calcular(self, peso, distancia):
        return 15 + (peso * 5) + (distancia * 0.10)


class Pac(EstrategiaFrete):

    def calcular(self, peso, distancia):
        return 10 + (peso * 3) + (distancia * 0.05)


class RetirarNaLoja(EstrategiaFrete):

    def calcular(self, peso, distancia):
        return 0


class CalculadoraFrete:

    def __init__(self, estrategia):
        self.estrategia = estrategia

    def definir_estrategia(self, estrategia):
        self.estrategia = estrategia

    def calcular(self, peso, distancia):
        return self.estrategia.calcular(peso, distancia)


calculadora = CalculadoraFrete(Sedex())

# Dados da entrega
peso = 5
distancia = 100

print(f"Sedex: R$ {calculadora.calcular(peso, distancia):.2f}")

calculadora.definir_estrategia(Pac())
print(f"PAC: R$ {calculadora.calcular(peso, distancia):.2f}")

calculadora.definir_estrategia(RetirarNaLoja())
print(f"Retirada: R$ {calculadora.calcular(peso, distancia):.2f}")