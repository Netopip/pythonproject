'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.'''



def main():
    vetor_par = []
    vetor_impar = []
    vetor_inteiro = []

    for i in range(20):
        numero = int(input('Digite um numero inteiro: ').strip())
        if numero % 2 == 0:
            vetor_par.append(numero)
            vetor_inteiro.append(numero)
        else:
            vetor_impar.append(numero)
            vetor_inteiro.append(numero)

    print(f'Vetor com números pares: {vetor_par}\nVetor com numeros ímpares: {vetor_impar}\nTodos os números: {vetor_inteiro}')

if __name__ == '__main__':
    main()

