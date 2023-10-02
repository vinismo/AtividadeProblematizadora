from abc import ABC, abstractmethod
from srcs.formaGeometrica import FormaGeometrica


class Retangulo(FormaGeometrica): #classe retangulo
    def __init__(self, cor, lado1, lado2): #superclasse
        super().__init__(cor)
        self.__lado1 = lado1
        self.__lado2 = lado2

    @property
    def lado1(self): #acessa lado1
        return self.__lado1

    @property
    def lado2(self): #acessa lado2
        return self.__lado2

  
    def calcularArea(self): #calcula area
        return self.__lado1 * self.__lado2

    def calcularPerimetro(self): #calcula perimetro
        return 2 * (self.__lado1 + self.__lado2)

    def exibirDados(self): #mostra dados
        return (
            f"O retângulo de cor {self.cor} com medidas {self.__lado1} e {self.__lado2} "
            f"tem área = {self.calcularArea()} e tem perímetro = {self.calcularPerimetro()}."
        )