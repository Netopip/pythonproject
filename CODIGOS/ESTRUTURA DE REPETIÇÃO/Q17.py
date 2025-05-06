import math


def main():
    while True:
        numero = int(input('Digite um numero interio: '))
        if numero > 0:
            fatorial = math.factorial(numero)
            print(fatorial)
        elif numero == 0:
            print('Programa encerrado!')
            break


if __name__ == '__main__':
    main()