'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58'''


while True:
    altura = float(input('Digite a sua altura: ').strip())
    ideal = (72.7 * altura) - 58
    print(f'O seu peso ideal é {ideal:.2f}kg')
    while True:
        res = str(input('Quer continuar(S para sim e N para Não). ')).upper().strip()
        if res in 'Ss':
            print('vamos continuar!')
            break
        elif res in 'Nn':
            break
        else:
            print('Digite algo válido!')
    if res == 'N':
        break

print('Acabamos por aqui!')

