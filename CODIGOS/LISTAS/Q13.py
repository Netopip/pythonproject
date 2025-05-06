'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''

def return_media(temperaturas):
    media = sum(temperaturas) / len(temperaturas)
    return round(media,2)

def acima_media(temperaturas, media):
    mes = 'Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'
    for indice,temp in enumerate(temperaturas):
        if temp > media:
            print(f'Temperatura de {temp} no mês de {mes[indice]}')
            
    
           

def main():
    temperaturas = list()
    
    for i in range(12):
        temp = float(input(f'Digite a temperatura do mes {i+1}: ').strip())
        temperaturas.append(temp)
        
    media = return_media(temperaturas)
    print(f'A temperatura média anual: {media} ºC')
    print('Meses com a temperatura acima da média:')
    acima_media(temperaturas,media)
    
        
        
if __name__ == '__main__':
    main()