import math

def main():
    while True:
        numero = int(input('Digite um numero interio entre 0 a 16: '))
        if 0 < numero < 16:
            fatorial = math.factorial(numero)
            print(fatorial)
        elif numero == 0:
            print('Programa encerrado!')
            break
        else:
            print('Digite um numero dentro do intervalo')



if __name__ == '__main__':
    main()