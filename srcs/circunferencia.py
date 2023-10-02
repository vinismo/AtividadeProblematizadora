from abc import ABC, abstractmethod
from srcs.formaGeometrica import FormaGeometrica
import math

class Circunferencia(FormaGeometrica): #classe crcunferência
    def __init__(self, cor, raio): #superclasse
        super().__init__(cor)
        self.__raio = raio

    def calcularArea(self): #calcula área
        return math.pi * math.pow(self.__raio, 2)

    def calcularPerimetro(self): #calcula perímetro
        return 2 * math.pi * self.__raio

    def exibirDados(self): #mostra dados
        return (
            f"A circunferência de cor {self.cor} com raio {self.__raio} "
            f"tem área = {self.calcularArea():.2f} e tem perímetro = {self.calcularPerimetro():.2f}."
        )