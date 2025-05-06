def reajuste_sal(salario):
    if salario <= 280:
        percentual = 20/100
        novo_salario = salario + (salario * percentual)
        aumento = novo_salario - salario
        return novo_salario,percentual,aumento
    elif salario < 700:
        percentual = 15/100
        novo_salario = salario + (salario * 15/100)
        aumento = novo_salario - salario
        return novo_salario,percentual,aumento
    elif salario < 1500:
        percentual = 10/100
        novo_salario = salario + (salario * percentual)
        aumento = novo_salario - salario
        return novo_salario,percentual,aumento
    elif salario >= 1500:
        percentual = 5/100
        novo_salario = salario + (salario * percentual)
        aumento = novo_salario - salario
        return novo_salario,percentual,aumento


def main():
    salario = float(input('Digite o seu salario: '))

    novo_salario, percentual, aumento = reajuste_sal(salario)
    print(f'O seu salario inicial de R${salario:.2f},com percentual de {percentual*100:.0f}% aumentou em R${aumento:.2f} o seu salario, ficando assim com o novo total de R${novo_salario:.2f}')

if __name__ == '__main__':
    main()