def media_idade(lista):
    if len(lista) == 0:
        return 0
    media = sum(lista) / len(lista)
    return media



def main():
    lista = []
    while True:
        entrada = str(input('Digite sua idade: '))
        try:
            idade = int(entrada)
            if idade > 0:
                lista.append(idade)
            else:
                print('Digite uma idade válida.')
        except ValueError:
            print('Por favor, digite um numero inteiro válido.')
        opcao = input('Deseja continuar? Digite "sair" para terminar o prigrama ou qualquer tecla para continuar').lower()
        if opcao == 'sair':
            break

    if lista:
        msg = media_idade(lista)
        print(msg)
    else:
        print('Nenhuma idade válida.')


if __name__ == '__main__':
    main()