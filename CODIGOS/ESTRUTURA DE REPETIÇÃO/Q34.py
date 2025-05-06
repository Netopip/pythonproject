'''Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.'''



def main():
    cont = 0
    numero = int(input('Digite um número: '))
    for i in range(1, numero +1):
        if numero % i == 0:
            cont += 1
    if cont == 2:
        print('É primo')
    else:
        print('Não é primo')
        
if __name__ == '__main__':
    main()