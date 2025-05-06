'''Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.'''
def soma_vetor(vetor):
    soma = 0
    for valor in vetor:
        soma += valor
    return soma

def multiplicacao(vetor):
    multi = 1
    for valor in vetor:
        multi *= valor
    
    return multi     
    
    
def main():
    vetor = []
    
    for i in range(5):
        numero = int(input('Digite um numero inteiro: ').strip())
        vetor.append(numero)
    
    soma = soma_vetor(vetor)
    multi = multiplicacao(vetor)   
    print(vetor)
    print(f'A soma dos numros do vetor é {soma}\nA multiplicação dos números dos vetores é {multi}.')
    
    
    
if __name__ == '__main__':
    main()