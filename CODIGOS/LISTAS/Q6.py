'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.'''
def media_aluno(matriz):
    matriz_media = []

    for aluno in matriz:
        media = sum(aluno) / len(aluno)
        matriz_media.append(round(media,2))

    return matriz_media

def main():
    matriz = []

    for i in range(10):
        linha = []
        for j in range(4):
            while True:
                try:
                    nota = float(input(f'Digite a {j +1} nota: ').strip())
                    if 0 < nota <= 10:
                        linha.append(nota)
                        break
                    else:
                        print('Nota inválida!')
                except ValueError:
                    print('Entrada Inválida!Por favor, digite um número.')

        matriz.append(linha)
    matriz_media = media_aluno(matriz)

    for i,media in enumerate(matriz_media):
        print(f'Aluno {i + 1} : {media}')


if __name__ == '__main__':
    main()