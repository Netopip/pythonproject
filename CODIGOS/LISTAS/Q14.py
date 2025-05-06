'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

def retornar_culpa(lista_respostas):
    if lista_respostas.count('SIM') == 5:
        print('CULPADO!')
    elif lista_respostas.count('SIM') == 3 or 4:
        print('CUMPLICE!')
    elif lista_respostas.count('SIM') == 2:
        print('SUSPEITO')
    else:
        print('INOCENTE')
    
def main():
    lista_respostas = []
    
    print('Responda as seguintes perguntas:(responda com sim/não)')
    
    perguntas = ['Telefonou para a vítima?',
                 'Esteve no local do crime?',
                 'Mora perto da vítima?',
                 'Devia para a vítima',
                 'Já trabalho com a vítima?'
                 ]
    
    for pergunta in perguntas:
        resposta = ''
        while resposta not in ['SIM', 'NÃO']:
            resposta = input(f'{pergunta}\n').strip().upper()
            if resposta not in ['SIM','NÃO']:
                print(f'Resposta inválida, responda com sim ou não.')
        lista_respostas.append(resposta)
    
    print('Repostas:',lista_respostas)
    print('Você é considerado: ')
    retornar_culpa(lista_respostas)
    
    
if __name__ == '__main__':
    main()