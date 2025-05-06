def maior_menor(n1, n2, n3):
    maior = max(n1, n2 ,n3)
    menor = min(n1, n2 ,n3)
    return maior, menor

def main():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())

    maior, menor = maior_menor(num1, num2, num3)

    print(f'O maior valor entre os numeros digitados {num1}, {num2} e {num3} é {maior}'
          f' e o menor é {menor}')

if __name__ == '__main__':
    main()