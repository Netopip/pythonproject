'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''
from math import pi

def calcular_area_circulo(raio):
    area = pi * (raio ** 2)
    print(f'A área dep círculo de raio {raio} é {area:.2f}cm²')
def main():
    
    raio = float(input('Digite o tamanho do raio:(em cm)\n'))
    
    calcular_area_circulo(raio)
    
if __name__ == '__main__':
    main()