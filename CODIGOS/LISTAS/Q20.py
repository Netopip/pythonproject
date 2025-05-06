'''As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00'''

def calcular_novo_salario(salarios):
    lista_novo_salario = []
    cont = 0
    for i in salarios:
        if (20/100)* i < 100:
            lista_novo_salario.append(i + 100)
            cont += 1
        else:
            lista_novo_salario.append(i + (i * (20/100)))
    return lista_novo_salario, cont

def calcular_valor_abono(salarios,lista_novo_salario):
    valor_abono = []
    for i in range(len(salarios)):
        abono = lista_novo_salario[i] - salarios[i]
        valor_abono.append(abono)
    maior_abono = max(valor_abono)
    return valor_abono,maior_abono

def main():
    salarios = []
    
    while True:
        try:
            entrada = input('Digite o seu salario:\n').strip()
            salario = float(entrada)
            if salario == 0:
                break
            elif salario < 0:
                print('Salário não pode ser menor que zero!')
            else:
                salarios.append(salario)
                
        except ValueError:
            print('Entrada inválida.')
    
    
    lista_novo_salario, cont= calcular_novo_salario(salarios)
    valor_abono,maior_abono = calcular_valor_abono(salarios,lista_novo_salario)
    print('SALARIO ------ ABONO')
    for i,salario in enumerate(salarios):
        print(f'R$ {salario:.2f} - {valor_abono[i]:.2f}')
    print(f'Foram processados {len(salarios)} colaboradores')
    print(f'Total de gastos com abonos: R$ {sum(valor_abono):.2f}.')
    print(f'O valor minimo pago a {cont} colaboradores.')
    print(f'Maior valor pago de abono foi de: R$ {maior_abono:.2f}')
    print('NOVOS SALARIOS:')
    for i,salario in enumerate(salarios):
        print(f'R$ {salario:.2f} -- R$ {lista_novo_salario[i]:.2f}')
    
    

if __name__ == '__main__':
    main()
                
    