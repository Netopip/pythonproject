def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    if media == 10:
        return (f'Com a média {media}. Aprovado com distinção!')
    elif media >= 7:
        return (f'Com a média {media}. Aprovado!')
    else:
        return (f'Com a média {media}. REPROVADO!')




def main():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))

    resultado = calcular_media(n1, n2)

    print(resultado)

if __name__ == '__main__':
    main()
