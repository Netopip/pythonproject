'''Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.'''


def somaImposto(taxa,custo):
    novo_valor = custo + (custo * taxa/100)
    return novo_valor    
    
    
def main():
    taxa_ = []
    custo_ = []
    while True:
        t = str(input('Quanto será a taxa(em %):\n').strip())
        c = str(input('Qual o custo do produto:\n').strip())
        try:
            taxa = float(t)
            custo = float(c)
            if taxa < 0 or custo < 0:
                print('O valor não pode ser menor que zero, tente novamente!')
            else:
                taxa_.append(taxa)
                custo_.append(custo)
                break
        except ValueError:
            print('Entrada inválida.')
            
    novo_valor = somaImposto(*taxa_,*custo_)
    print(f'Com a taxa de {taxa_[0]:.2f}% e o custo de {custo_[0]:.2f} o novo valor de custo do produto é R$ {novo_valor:.2f}.')
    
    
if __name__ == '__main__':
    main()        