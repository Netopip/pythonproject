'''Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.'''
def media_alturas(dados):
    soma_alturas = 0
    cont_alturas = 0
    for linha in dados:
        soma_alturas += linha[1]
        cont_alturas += 1
    
    media = soma_alturas / cont_alturas
    return round(media,2)

def alunos_abaixo_media(dados, media):
    lista_alunos_abaixo = []
    for alunos in dados:
        if alunos[0] < 13 and alunos[1] < media:
            lista_alunos_abaixo.append(alunos)
    return lista_alunos_abaixo

def main():
    
    dados = []
    
    for i in range(5):
        idade = int(input('Sua idade: ').strip())
        altura = float(input('Sua altura: ').strip())
        dados.append([idade,altura])
        
    
    media = media_alturas(dados)
    lista_alunos_abaixo = alunos_abaixo_media(dados,media)
    print(media)
    print(len(lista_alunos_abaixo))
    
if __name__ =='__main__':
    main()