def soma_media(lista):
    soma = sum(lista)
    media = sum(lista)/len(lista)
    return soma, media


def main():
    lista = list()
    for i in range(5):
        numero = int(input('Digite um número: '))
        lista.append(numero)
        
        
    soma, media = soma_media(lista)
    print(f'A soma dos numeros é {soma} e a média é {media:.2f}. ')

if __name__ == '__main__':
    main()


