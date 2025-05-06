def intervalo(num1, num2):
    lista = list(range(num1,num2))
    soma = sum(lista)
    return soma




def main():
    num1 = int(input())
    num2 = int(input())

    soma = intervalo(num1, num2)
    print(f'A soma dos valores no intervalo de {num1} e {num2} é {soma}.')

if __name__ == '__main__':
    main()
