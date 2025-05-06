'''Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.'''
def vetor_inverso(vetor):
    vetor = sorted(vetor, reverse=True)
    print(vetor)

def main():
    vetor = []

    for i in range(10):
        numero = int(input('Digite um numero inteiro: ').strip())
        vetor.append(numero)

    vetor_inverso(vetor)

if __name__ == '__main__':
    main()

