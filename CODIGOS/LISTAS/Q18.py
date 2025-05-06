'''Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.'''


def total_de_votos(votos):
    total_votos = len(votos)
    return total_votos

def votos_por_jogadores(votos, numero_jogador):
    #dicionario com o numero do jogador e zero nos votos
    contagem_votos = {jogador: 0 for jogador in numero_jogador}
    
    for voto in votos:
        if voto in contagem_votos:
            contagem_votos[voto] += 1
        
    return contagem_votos
    
def porcentagem_votos_jogadores(contagem_votos,total_votos):
    porcentagens = {}
    for jogador, votos in contagem_votos.items():
        if total_votos > 0:
            porcentagens[jogador] = (votos/total_votos) *100
        else:
            porcentagens[jogador] = 0
    return porcentagens
    

def main():
    votos = []
    numero_jogador = list(range(1,24))
    while True:
        try:
            votacao = str(input('Digite o seu voto:').strip())
            voto = int(votacao)
            if voto < 0 or voto > 23:
                print('Voto Inválido.')
                continue
            elif voto == 0:
                break
            else:
                votos.append(voto)
        except ValueError:
            print('Entrada inválida.Digite um numero dentro do intervalo.')
            
    total_votos = total_de_votos(votos)
    print(f'O total de votos computados foi de: {total_votos}')
    
    contagem_votos = votos_por_jogadores(votos,numero_jogador)
    porcentagens = porcentagem_votos_jogadores(contagem_votos,total_votos) 
    
    for jogador in numero_jogador:
        print(f'Jogador {jogador}: {contagem_votos[jogador]} votos ({porcentagens[jogador]:.2f}% dos votos)')              
        
    print('O melhor jogador foi:')
    melhor= max(porcentagens, key=porcentagens.get)
    melhor_porc = porcentagens[melhor]
    
    print(f'O melhor jogador foi {melhor}, com {melhor_porc:.2f}% dos votos')
if __name__ =='__main__':
    main()
                
        

