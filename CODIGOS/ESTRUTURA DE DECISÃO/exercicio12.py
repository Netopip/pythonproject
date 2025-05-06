def calcular_folha(salario):
    if salario <= 900:
        ir = 'Isento'
        inss = salario * 10/100
        fgts = salario * 11/100
        desconto = inss
        salario_liquido = salario - desconto
        return ir,inss,fgts,desconto,salario_liquido
    elif salario <= 1500:
        ir = salario * 5/100
        inss = salario * 10/100
        fgts = salario * 11/100
        desconto = ir + inss
        salario_liquido = salario - desconto
        return ir, inss, fgts, desconto, salario_liquido
    elif salario <= 2500:
        ir = salario * 10 / 100
        inss = salario * 10 / 100
        fgts = salario * 11 / 100
        desconto = ir + inss
        salario_liquido = salario - desconto
        return ir, inss, fgts, desconto, salario_liquido
    elif salario > 2500:
        ir = salario * 20 / 100
        inss = salario * 10 / 100
        fgts = salario * 11 / 100
        desconto = ir + inss
        salario_liquido = salario - desconto
        return ir, inss, fgts, desconto, salario_liquido


def main():
    horas = int(input('Quantas horas você trabalhou nesse mês: '))
    valor_hora = float(input('Qual o valor da sua hora de trabalho: R$ '))

    salario_bruto = horas * valor_hora

    ir,inss,fgts,desconto,salario_liquido = calcular_folha(salario_bruto)
    print(f'Com um salario bruto de: R${salario_bruto:.2f}\nImposto de renda será de: R$ {ir}\nINSS de : R${inss:.2f}\nFGTS de : R${fgts:.2f}\nCom descontos totais de: R${desconto} (R${ir} + R${inss})\nSalario liquido de : R${salario_liquido:.2f}')

if __name__ == '__main__':
    main()