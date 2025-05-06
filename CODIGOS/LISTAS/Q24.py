'''Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
'''
from random import randint

def quantidade_numero(dados_lancados):
    quantidade_vezes = []
    numero = []
    
    for i in range(1,7):
        numero.append(i)
        quant = dados_lancados.count(i)
        quantidade_vezes.append(quant)
    
    for i in range(len(numero)):
        print(f'Numero {numero[i]}: apareceu {quantidade_vezes[i]} vezes')
                        
    
def main():
    dados_lancados = []
    
    for i in range(100):
        numero = randint(1,6)
        dados_lancados.append(numero)
        
    quantidade_numero(dados_lancados)

if __name__ == '__main__':
    main()