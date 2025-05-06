def tabuada(numero):
    print(f'A tabuada no numero {numero} :')
    for i in range(1,11):
        print(f'{numero} * {i} = {numero * i}')

def main():
    numero = int(input())

    tabuada(numero)

if __name__ == '__main__':
    main()