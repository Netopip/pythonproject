def verificar_numeros(a, b, c, d):
    if (b > c) and (d > a) and (c + d > a + b) and (c > 0) and (d > 0) and (a % 2 == 0):
        return 'Valores aceitos'
    else:
        return 'Valores nao aceitos'


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    msg = verificar_numeros(a,b,c,d)
    print(msg)

if __name__ == '__main__':
    main()