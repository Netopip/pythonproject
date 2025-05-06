'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

valor_hora = float(input('Qual o valor da sua hora de trabalho:'))
horas_dia= float(input('Quantas horas voce trabalho no dia: '))
dias_trabalhados = int(input('Quantos dias você trabalhou este mês: '))

valor_diaria = valor_hora * horas_dia
salario = valor_diaria * dias_trabalhados

print(f'O seu salário no final do mês será de R$ {salario:.2f}, já que você trabalhou {dias_trabalhados} dias, e sua diária é no valor de R$ {valor_diaria:.2f}')




