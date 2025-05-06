def calcular_media(*notas):
    media = sum(notas) / len(notas)
    if media >= 9:
        return ['A', media, 'APROVADO']
    elif media >= 7.5:
        return ['B', media, 'APROVADO']
    elif media >= 6:
        return ['C', media, 'APROVADO']
    elif media >= 4:
        return ['D', media, 'REPROVADO']
    elif media >= 0:
        return ['E', media, 'REPROVADO']
    else:
        return 'MÉDIA INVÁLIDA'

def main():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))

    resultado = calcular_media(n1,n2)
    print(f'Notas: {n1}, {n2} | Média: {resultado[1]} | Conceito: {resultado[0]} | resultado:{resultado[2]}')

if __name__ == '__main__':
    main()

    #poderia ser utilizado outro metodo para a verificação deo resultado aprovado