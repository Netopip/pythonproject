'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120'''
        
def main():
    numero = int(input('Diigte um numero inteiro: '))
    total = 1

    for i in range(1, numero + 1):
        total *= i
        
    print(f'Fatorial de: {numero} = {total}')
    
    
     
if __name__=='__main__':
    main()
    