from abc import ABC, abstractmethod
import math


class Forma(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio


def calcular_formas(formas):
    soma_areas = 0
    soma_perimetros = 0

    for forma in formas:
        soma_areas += forma.area()
        soma_perimetros += forma.perimetro()

    print(f"Soma das áreas: {soma_areas:.2f}")
    print(f"Soma dos perímetros: {soma_perimetros:.2f}")


retangulo = Retangulo(10, 5)
circulo = Circulo(3)

lista_formas = [retangulo, circulo]

calcular_formas(lista_formas)