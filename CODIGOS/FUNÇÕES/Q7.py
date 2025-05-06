'''Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.'''

def valorPagamento(prestacao, atraso):
    total_prestacoes = []
    quant_prestacao = len(total_prestacoes)
    
    if atraso == 0:
        print(f'O valor da prestação será R$ {prestacao:.2f} pois não houve atraso!')
        
    else:
        multa = ((3/100) * prestacao) 
        juros = ((0.1/100) * prestacao) * atraso
        valor_a_pagar = prestacao + multa + juros
        print(f'O valor total a pagar será de R$ {valor_a_pagar:.2f} pois houve um atraso de {atraso} dias e multa.')
    
    
    
    
def main():
   
    while True:
        prestacao = str(input('Qual o valor da prestação?\n').strip())
        dias_atraso = str(input('Quantos dias esta atrasada?\n').strip())
        try:
            n_prestacao = float(prestacao)
            n_atraso = int(dias_atraso)
            if n_prestacao < 0 or n_atraso < 0:
                print('O valor não poder ser menor que zero, digite um numero positivo.')# os valores nao podem ser negativos
                continue #reinicia o loop
            else:
                valorPagamento(n_prestacao,n_atraso)
        except ValueError:
            print('Entrada inválida, tente novamente.') #trata a entrada errada nas variaveis n_prestaçoes e n_atraso
            continue #serve para reiniciar o loop
      
        while True:
            opcao = str(input('Quer continuar? (SIM/NÃO)\n').strip()).upper()
            if opcao == 'SIM':
                break #encerra esse loop e volta pra o while principal
            elif opcao in ['NÃO','NAO']:
                print('Programa encerrado!')
                return # encerra o while principal tbm
            else:
                print('Opção inválida.')#trata as entradas invalidas para as opçoes
            
    
if __name__ == '__main__':
    main()      
        