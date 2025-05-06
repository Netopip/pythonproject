def operacoes(lista):
    menor = min(lista)
    maior = max(lista)
    soma = sum(lista)
    return menor, maior, soma




def main():
    lista = []
    while True:
        numero = float(input('Digite um numero entre 0 e 1000: '))
        if 0 < numero < 1000:
            lista.append(numero)
        elif numero == 0:
            break
        else:
            print('Digite um numero valido.')
    menor, maior, soma = operacoes(lista)
    print(f'O menor valor da lista é {menor}, o maior {maior} e a soma do conjunto de numeros é {soma}.')

if __name__ == '__main__':
    main()