'''seguinte fórmula: (72.7*altura) - 58
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

while True:
    altura = float(input('Digite a sua altura: '))
    sexo = str(input('Qual o seu sexo:[M/F] ')).upper().strip()
    if sexo == 'M':
        ideal = (72.7 * altura) - 58
        print(f'O seu peso ideal é de {ideal:.2f}')
    elif sexo == 'F':
        ideal = (62.1 * altura) - 44.7
        print(f'O seu peso ideal é de {ideal:.2f}')
    else:
        print('Digite algo válido.')
    while True:
        resp = str(input('Voce quer continuar:[S/N] ')).upper().strip()
        if resp == 'S':
            print('Vamos continuar!')
            break
        elif resp == 'N':
            break
        else:
            print('Digite algo valido.')
    if resp == 'N':
        break

print('Encerramos por aqui')




