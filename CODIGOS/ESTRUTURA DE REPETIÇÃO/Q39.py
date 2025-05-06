'''Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.'''


def alunos_mais_alto(lista_alunos):
    numero_mais_alto = lista_alunos[0][0]
    mais_alto = lista_alunos[0][1]
    
    for aluno in lista_alunos:
        if aluno[1] > mais_alto:
            mais_alto = aluno[1]
            numero_mais_alto = aluno[0]
            
    return numero_mais_alto, mais_alto


def aluno_mais_baixo(lista_alunos):
    numero_mais_baixo = lista_alunos[0][0]
    mais_baixo = lista_alunos[0][1]
    
    for aluno in lista_alunos:
        if aluno[1] < mais_baixo:
            mais_baixo = aluno[1]
            numero_mais_baixo = aluno[0]
    return numero_mais_baixo,mais_baixo
        
    


def main():
    lista_alunos = []
    for i in range(3):
        numero = int(input('Digite seu número: '))
        altura = float(input('Digite a sua altura:(em cm) '))
        lista_alunos.append([numero,altura])
        
    numero_mais_alto, mais_alto = alunos_mais_alto(lista_alunos)
    numero_mais_baixo,mais_baixo = aluno_mais_baixo(lista_alunos)
    print(f'O número do mais alto é {numero_mais_alto} com alturqa de  {mais_alto}cm')
    print(f'O número do mais baixo é {numero_mais_baixo} com altura de {mais_baixo}cm')
        
    
    
if __name__=='__main__':
    main()