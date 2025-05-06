def media_lista(lista):
    media_total = sum(lista)/ len(lista)
    return media_total


def main():
    lista = []
    while True:
        numero = float(input('Digite uma nota: '))
        if 0 < numero <= 10:
            lista.append(numero)
        elif numero == 0:
            break
        else:
            print('Nota inválida.')

    msg = media_lista(lista)
    print(f'Os notas da lista são {lista} e a media aritmética das notas é {msg:.2f}.')


if __name__ == '__main__':
    main()