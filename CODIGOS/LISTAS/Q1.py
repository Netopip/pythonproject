'''Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.'''

def main():
    vetor = []

    for i in range(5):
        numero = int(input('Digite um numero:').strip())
        vetor.append(numero)

    print(vetor)

if __name__ == '__main__':
    main()