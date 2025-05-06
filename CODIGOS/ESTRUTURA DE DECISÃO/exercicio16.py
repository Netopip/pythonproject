import math

def calcular_raiz():
    a = float(input('Informe o valor de A: '))
    if a == 0:
        print('A equação não é do segundo grau!')
        return
    b = float(input('Informe o valor de B: '))
    c = float(input('Informe o valor de C: '))

    delta = b**2 -4 * a * c
    if delta < 0:
        print('A equação não possui raizes reais!')
    elif delta == 0:
        raiz = -b / (2*a)
        print(f'A equação possui apenas uma raiz real : {raiz}')
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f'A equação possui 2 raizes reaias : {raiz1:.2f} e {raiz2:.2f}')
calcular_raiz()