def decrescente(numeros):
    ordem = sorted(numeros, reverse=True)
    return ordem



def main():
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())

    numeros = n1 , n2, n3
    ordem = decrescente(numeros)

    print(f'Os numeros digitados em ordem decrescente é :{ordem}')

if __name__ == '__main__':
    main()