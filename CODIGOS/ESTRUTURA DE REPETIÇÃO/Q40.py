'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.'''
def maior_indice_acidente(estatistica_cidades):
    maior_i_acidentes = estatistica_cidades[0][2]
    cidade_maior_i = estatistica_cidades[0][0]
    
    for cidade in estatistica_cidades:
        if cidade[2] > maior_i_acidentes:
            maior_i_acidentes = cidade[2]
            cidade_maior_i = cidade[0]
            
    return maior_i_acidentes,cidade_maior_i


def menor_indice_acidente(estatistica_cidades):
    menor_i_acidentes = estatistica_cidades[0][2]
    cidade_menor_i = estatistica_cidades[0][0]
    
    for cidade in estatistica_cidades:
        if cidade[2] < menor_i_acidentes:
            menor_i_acidentes = cidade[2]
            cidade_menor_i = cidade[0]
            
    return menor_i_acidentes,cidade_menor_i

def media_acidentes(estatistica_cidades):
    acidentes = []    
    for cidade in estatistica_cidades:
        acidentes.append(cidade[2])
    media = sum(acidentes)/len(acidentes)
    
    return round(media,2)

def media_acidentes_menos_2000v(estatistica_cidades):
    cidades_menos_2000 = []
    
    for cidade in estatistica_cidades:
        if cidade[1] < 2000:
            cidades_menos_2000.append(cidade[2])
    media_menos_2000 = sum(cidades_menos_2000)/ len(cidades_menos_2000)
    
    return round(media_menos_2000,2)
            

def main():
    estatistica_cidades = []
    for i in range(5):
        codigo_cidade = int(input('O códiog da cidade:\n').strip())
        numero_veiculos = int(input('O total de veículos de passeio:\n').strip())
        numeros_acidentes = int(input('Nuúmero de acidentes com vítimas:\n').strip())
        estatistica_cidades.append([codigo_cidade,numero_veiculos,numeros_acidentes])
        
    
    maior_i_acidentes,cidade_maior_i = maior_indice_acidente(estatistica_cidades)
    menor_i_acidentes,cidade_menor_i = menor_indice_acidente(estatistica_cidades)
    media = media_acidentes(estatistica_cidades)
    media_menos_2000 = media_acidentes_menos_2000v(estatistica_cidades)
    print(f'O maior indice de acidentes foi na cidade {cidade_maior_i} com o números de {maior_i_acidentes} acidentes.')
    print(f'O menor indice de acidentes foi da cidade {cidade_menor_i} com o númeor de {menor_i_acidentes}')
    print(f'A média de acidentes entre as cidades foi de {media} acidentes.')
    print(f'A média de acidentes das cidades em que o numero de veículos é menor que 2000 é {media_menos_2000}.')
    
    
    
if __name__=='__main__':
    main()