'''Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.'''

def modelo_mais_economico(carros,consumos):
    mais_economico = consumos[0]
    carro_mais_economico = carros[0]
    for i,consumo in enumerate(consumos):
        if consumo > mais_economico:
            mais_economico = consumo
            carro_mais_economico = carros[i]
    print(f'O carro mais econimico é {carro_mais_economico} com o consumo de {mais_economico}km/l ')
    
def calcular_distancia_1000(carros,consumos):
    lista_litros_necessario = []
    custo_total = []
    km = 1000
    valor_litro = 2.25
    for i in consumos:
        litros = 1000/i
        lista_litros_necessario.append(round(litros,2))
    for j in lista_litros_necessario:
        total = j * valor_litro
        custo_total.append(round(total,2))
    
    for indice,carro in enumerate(carros):
        print(f'{indice + 1} - {carro}  -  {consumos[indice]}\n{lista_litros_necessario[indice]} - R$ {custo_total[indice]}')
        
        


def main():
    carros = []
    consumos = []
    
    for i in range(5):
        carro = str(input(f'Digite o {i+1} carro:\n').strip())
        carros.append(carro)
        consumo = float(input(f'Digite o consumo do {carros[i]}:\n').strip())
        consumos.append(consumo)
    
    print('COMPARATIVO DE CONSUMO DE COMBUSTÍVEL:')
    for i,carro in enumerate(carros):
        print(f'Veículo {i+1}\nNome: {carro}\nKm por litro: {consumos[i]}')
    
    print('Relatório final:')
    calcular_distancia_1000(carros,consumos)
    modelo_mais_economico(carros,consumos)

if __name__ == '__main__':
    main()