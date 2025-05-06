'''Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.'''

def soma_dos_quadrados(vetor):
    soma = 0
    for i in vetor:
        soma += i**2
    print (soma)
    

def main():
    
    vetor = [] #conjunto de numeros adicionados durante o for de 10 numeros
    
    for i in range(10):
        number = int(input())
        vetor.append(number)
        
    soma_dos_quadrados(vetor)
    
if __name__ == '__main__':
    main()
    