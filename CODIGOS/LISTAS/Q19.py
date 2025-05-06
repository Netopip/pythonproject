'''Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.'''

def contagem_votos(votacao):
    lista_contagem_votos = []
    for i in range(1,7):
        lista_contagem_votos.append(votacao.count(i))
    
    return lista_contagem_votos

def porcentagem_votos(lista_contagem_votos,votacao):
    lista_porcentagem = []
    total = len(votacao)
    for voto in lista_contagem_votos:
        lista_porcentagem.append((voto/total)*100)
    
    return lista_porcentagem
    
def main():
    votacao = []
    
    while True:
        print('Qual o melhor Sistema Operacional para uso em servidores?\n'

                'As possíveis respostas são:\n'

                '1- Windows Server\n'
                '2- Unix\n'
                '3- Linux\n'
                '4- Netware\n'
                '5- Mac OS\n'
                '6- Outro')
        try:
            entrada = input('Digite seu voto:\n').strip()
            voto = int(entrada)
            if voto < 0 or voto > 6:
                print('Voto inválido')
            elif voto == 0:
                break
            else:
                votacao.append(voto)
            
        except ValueError:
            print('Entrada inválida, digite um numero para votar.')
    
    print(f'Total de votos: {len(votacao)}')
    lista_contagem_votos = contagem_votos(votacao)
    lista_porcentagem = porcentagem_votos(lista_contagem_votos,votacao)
    sistemas = ['Windows Server',' Unix','Linux','Netware','Mac OS','Outro']
    for i,sistema in enumerate(sistemas):
        print(f'{sistema}     {lista_contagem_votos[i]} voto(s)\n{lista_porcentagem[i]:.2f}%')
    
if __name__ == '__main__':
    main()
