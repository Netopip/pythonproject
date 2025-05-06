'''Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.'''

def contagem_numeros(lista):
    cont_0_25 = 0
    for i in lista:
        if 0 <= i <= 25:
            cont_0_25 += 1
    print(f'A qauntidade de números digitados que estão entre 0 e 25 é {cont_0_25}.')
    
    cont_26_50 = 0
    for i in lista:
        if 26 <= i <= 50:
            cont_26_50 += 1
    print(f'A qauntidade de números digitados que estão entre 16 e 50 é {cont_26_50}.')
    
    cont_51_75 = 0 
    for i in lista:
        if 51 <= i <= 75:
            cont_51_75 += 1
    print(f'A qauntidade de números digitados que estão entre 51 e 75 é {cont_51_75}.')
    
    cont_76_100 = 0
    for i in lista:
        if 76 <= i <= 100:
            cont_76_100 += 1
    print(f'A qauntidade de números digitados que estão entre 76 e 100 é {cont_76_100}.')
    
                


def main():
    
    numeros = list()
    while True:
        
        number = int(input('Digite um número: Use numeros negativos para sair ').strip())
        if number < 0:
            break
        else:
            numeros.append(number)
            
    contagem_numeros(numeros)
    
if __name__ == '__main__':
    main()