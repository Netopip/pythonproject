def par(num):
    if num % 2 == 0:
        return 'PAR'
    else:
        return 'IMPAR'

def main():
    num = int(input('Digite um numero: '))

    msg = par(num)
    print(f'O numero {num} é {msg}')

if __name__ == '__main__':
    main()