'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m'''

def main():
    
    competidores = []
    
    while True:
        nome = str(input('Atleta: ').strip())
        if nome == '':
            break
        saltos = []
        for i in range(5):
            salto = float(input(f'{i+1}º salto: ').strip())
            saltos.append(salto)
        competidores.append([nome,saltos])
    
    
    for atleta in competidores:
        nome = atleta[0]
        saltos = atleta[1]
        print(f'Atleta: {nome}\n')
        print(f'Primeiro salto: {saltos[0]}m')
        print(f'Segundo salto: {saltos[1]}m')
        print(f'Terceiro salto: {saltos[2]}m')
        print(f'Quarto salto: {saltos[3]}m')
        print(f'Quinto salto: {saltos[4]}m')

        saltos_str = '-'.join([str(s) for s in saltos])
        media = sum(saltos)/ len(saltos)
        print(f'\nResultado final:\nAtleta: {nome}')
        print(f'Saltos: {saltos_str}')
        print(f'Média dos saltos: {media:.1f} m')
        

if __name__ == '__main__':
    main()
            