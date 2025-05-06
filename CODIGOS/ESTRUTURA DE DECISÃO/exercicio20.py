def calcular_media(*notas):
    media = sum(notas) / len(notas)
    if media == 10:
        situacao = 'APROVADO COM DISTINÇÃO'
        return media, situacao
    elif media >= 7:
        situacao = 'APROVADO'
        return media, situacao
    else:
        situacao = 'REPROVADO'
        return media, situacao


def main():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))

    media, situacao = calcular_media(n1, n2, n3)

    print(f'{situacao} : Com a média {media:.2f}.')

if __name__ == '__main__':
    main()