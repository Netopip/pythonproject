def é_triangulo(lado1, lado2, lado3):
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        return 'Um triangulo pode ser formado!'
    else:
        return 'Não poderá formar um triangulo'

def verificar_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return 'TRIANGULO ÉQUILATERO'
    elif lado1 == lado2 or lado3 == lado2 or lado1 == lado3:
        return 'TRIANGULO ISOCELES'
    #elif lado1 != lado2 != lado3 != lado1:
    #    return 'TRIANGULO ESCALENO'
    else:
        return 'TRIANGULO ESCALENO'


def main():
    lado1 = float(input('Digite um lado do triangulo: '))
    lado2 = float(input('Digite um lado do triangulo: '))
    lado3 = float(input('Digite um lado do triangulo: '))

    pode = é_triangulo(lado1, lado2, lado3)
    print(pode)

    if pode == 'Um triangulo pode ser formado!':
        tipo_triangulo = verificar_triangulo(lado1, lado2, lado3)
        print(tipo_triangulo)

if __name__ == '__main__':
    main()

