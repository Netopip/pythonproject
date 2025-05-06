'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.'''

def consoante_caracter(caracteres):
    consoantes = []

    for letra in caracteres:
        if letra in 'bcdfghjklmnpqrstvwxyz': #usa-se in em vez de ==, pois o == verificaria se a letra seria igual o conjunto de caracteres, enquanto in verifica se a letra esta contida na cadeia de caracteres.
            consoantes.append(letra)

    print(f'Foram lidas : {len(consoantes)}\nQue são elas: {consoantes}')

def main():
    caracteres = []

    for i in range(10):
        char = str(input('Digite um caracter: ').strip()).lower()
        caracteres.append(char)

    consoante_caracter(caracteres)

if __name__ == '__main__':
    main()