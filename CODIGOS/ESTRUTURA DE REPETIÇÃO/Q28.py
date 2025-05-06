'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''

def calcular_total_media(lista):
    media = sum(lista) / len(lista)
    total = sum(lista)
    return media, total


def main():
    lista = []
    quantidade_cds = int(input('Digite a quantidade de CDs comprados: '))
    for i in range(quantidade_cds):  
        valores_cds = float(input(f'Qual o valor do {i+1}º cd? '))
        lista.append(valores_cds)
    media, total = calcular_total_media(lista)
    print(f'O total investido em CDs foi de R${total:.2f}, e a média dos valores foi de {media:.2f}.')
    

if __name__ == '__main__':
    main()