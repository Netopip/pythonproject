'''Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:'''


def main():
    while True:
        numero = int(input(f'Montar a tabuada de:'))
        comeco = int(input('Começar por: '))
        fim = int(input('Terminar em: '))
        if comeco > fim:
            print(f'Valores errados, digite novamente!')
        else:
            print(f'Vou montar uma tabuada de {numero} começando em 4 e terminando em {fim} :')
            for i in range(comeco,fim+1):
                print(f'{numero} x {i} = {numero * i}')
            break
            
if __name__=='__main__':
    main()