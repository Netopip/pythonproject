'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.'''

def temperatura(temperatura):
    f = (temperatura * 9/5) + 32
    return f

def main():
    graus = float(input('Digite a temperatura em graus ºC: '))

    trans = temperatura(graus)
    print(f'A temperatura em ºC {graus} em Fharenheit é de {trans}ºF.')

if __name__ == '__main__':
    main()
