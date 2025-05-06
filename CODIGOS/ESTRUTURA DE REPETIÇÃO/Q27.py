'''Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.'''
def calcular_media(x,y):
    media = sum(x) / y
    return media

def main():
    alunos_por_turmas = []
    quan_turmas = int(input('Digite a quantidade de turmas: '))
    for i in range(quan_turmas):
        while True:
            quant_alunos = int(input('Digite a quantidade de alunos: '))
            if quant_alunos > 40:
                print('Quantidade acima do limite!')
            else:
                alunos_por_turmas.append(quant_alunos)
                break
    
    media = calcular_media(alunos_por_turmas, quan_turmas)
    print(f'A média de alunos por turmas é de {media:.2f}.')

if __name__ == '__main__':
    main()
            
    