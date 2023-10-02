from abc import ABC, abstractmethod
import math


class FormaGeometrica(ABC): #classe mãe
    def __init__(self, cor):
        self.__cor = cor  #atributi cor em capsulado

    @property
    def cor(self): #acessa cor
        return self.__cor

    def alterarCor(self, cor): #altera cor
        self.__cor = cor

    @abstractmethod
    def calcularArea(self): #classe filha
        pass

    @abstractmethod
    def calcularPerimetro(self): #classe filha
        pass

    @abstractmethod
    def exibirDados(self): #classe filha
        pass