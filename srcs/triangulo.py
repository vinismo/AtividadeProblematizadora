from abc import ABC, abstractmethod
from srcs.formaGeometrica import FormaGeometrica
import math


class Triangulo(FormaGeometrica): #classe trinagulo
    def __init__(self, cor, lado1, lado2, lado3): #superclasse
        super().__init__(cor)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    def calcularArea(self): #calcula área
        s = (self.__lado1 + self.__lado2 + self.__lado3) / 2
        return math.sqrt(s * (s - self.__lado1) * (s - self.__lado2) * (s - self.__lado3))
    
    def calcularPerimetro(self): #calcula perímetro
        return self.__lado1 + self.__lado2 + self.__lado3

    def exibirDados(self): #exibe dados
        return (
          f"O triângulo de cor {self.cor} com medidas {self.__lado1}, {self.__lado2}, e {self.__lado3} "
          f"tem área = {self.calcularArea():.2f} e tem perímetro = {self.calcularPerimetro():.2f}."
        )