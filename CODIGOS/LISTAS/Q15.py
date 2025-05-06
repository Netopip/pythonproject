'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;'''
def soma_media_notas(notas):
    media = sum(notas)/ len(notas)
    soma = sum(notas)
    
    return round(media,2),soma

def valores_acima_media(notas,media):
    valores_acima = []
    valores_abaixo = []
    for i in notas:
        if i > media:
            valores_acima.append(i)
    
    return valores_acima

def valores_abaixo_7(notas):
    valores_aba_7 = []
    for i in notas:
        if i < 7:
            valores_aba_7.append(i)
    return valores_aba_7
    

def main():
    notas = []
    while True:
        numero = float(input())
        if numero == -1:
            break
        else:
            notas.append(numero)
    
    lista_reversa = list(reversed(notas))
    media,soma = soma_media_notas(notas)
    valores_acima = valores_acima_media(notas,media)
    valores_aba_7 = valores_abaixo_7(notas)
        
    print(f'O total de valores lidos é: {len(notas)}')
    for i in notas:
        print(i,end=' ')
    print()
    print('Os valores lidos na ordem inversa um abaixo do outro:')
    for j in lista_reversa:
        print(j)
    print(f'A soma dos valores é: {soma}')
    print(f'A média dos valores da lista é: {media}')
    print(f'A qauntidade de valores acima da média é: {len(valores_acima)}\nQue são eles:')
    for k in valores_acima:
        print(k)
    print(f'A quantidade de valores abaixo de 7 é: {len(valores_aba_7)}\nQue são eles:')
    for h in valores_aba_7:
        print(h)
    print('GRAÇAS A DEUS ACABOU!')        
    
    
   
if __name__ == '__main__':
    main()