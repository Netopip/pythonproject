'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''


dinheiro = float(input('Quanto voce ganha por hora:\n'))
horas = int(input('Quantas horas trabalhadas no mês:\n'))
salario_bruto = dinheiro * horas
ir = salario_bruto * (11/100)
inss = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos
print(f'Seu salario bruto é R${salario_bruto}\nO imposto de renda é de R${ir}\nO desconto de inss é de R${inss}\nE de sindicato é de R${sindicato}\nTotalizando R${descontos} de desconto\nE seu salario liquido final é R${salario_liquido}')