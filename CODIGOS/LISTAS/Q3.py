'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela.'''
def media_notas(notas):
    media = sum(notas) / len(notas)
    return round(media,2)


def main():
    notas = []
    for i in range(4):
        nota = float(input(f'Digite a {i +1} nota: ').strip())
        notas.append(nota)

    media = media_notas(notas)
    for nota in notas:
        print(f'{nota} || ', end=' ')
    print(f'A média das notas : {media}')

if __name__ == '__main__':
    main()

