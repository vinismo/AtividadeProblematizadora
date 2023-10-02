from srcs.formaGeometrica import FormaGeometrica
from srcs.retangulo import Retangulo
from srcs.triangulo import Triangulo
from srcs.circunferencia import Circunferencia
import math

# retangulo1 = Retangulo("azul", 10, 20)
# print(f"O retângulo de lados {retangulo1.lado1} e {retangulo1.lado2} tem a cor {retangulo1.cor}.")
# print("Sua área é", retangulo1.calcularArea(), "e seu perímetro é", 
# retangulo1.calcularPerimetro(),".")

#----------------------------------------------------------------------------------------

# retangulo2 = Retangulo("vermelha", 3, 4)
# print(retangulo2.exibirDados())

#----------------------------------------------------------------------------------------

if __name__ == "__main__":

     print("Lista de Formas Geométricas:") #lista
     lista_formas = [
         Retangulo("azul", 10, 20),
         Retangulo("vermelha", 3, 4),
         Circunferencia("laranja", 2),
         Triangulo("rosa", 3, 4, 5)
     ]

     for forma in lista_formas: #mostra dados
         print(forma.exibirDados())