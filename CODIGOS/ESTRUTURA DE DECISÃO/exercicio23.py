def verificar_numero(numero):
    if numero % 1 == 0:
       return 'É inteiro'
    else:
        return 'É decimal'


def main():
    num = float(input('Digite um numero:'))
    msg = verificar_numero(num)
    print(msg)

if __name__ == '__main__':
    main()