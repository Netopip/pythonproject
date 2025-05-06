'''Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.'''

def positivo_negativo(num):
    if num <= 0:
        print('N')
    else:
        print('P')

def main():
    n = []
    while True:
        entrada = str(input('Digite um numero:\n').strip())
        try:
            numero = float(entrada)
            n.append(numero)
            break
            
        except ValueError:
            print('Entrada de dados inválida!')
    
    # a função recebe a lista descompactada para poder verificar se o numero contida nela satisfaz a condição na função.
    positivo_negativo(*n)
    
if __name__ == '__main__':
    main()
    