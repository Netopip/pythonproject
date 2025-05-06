'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes'''
def mais_alto(codigos,alturas,pesos):
    alunos_mais_alto = alturas[0]
    codigo_mais_alto = codigos[0]
    peso_mais_alto = pesos[0]
    for i in range(len(alturas)):
        if alturas[i] > alunos_mais_alto:
            alunos_mais_alto = alturas[i]
            codigo_mais_alto = codigos[i]
            peso_mais_alto = pesos[i]
    return alunos_mais_alto,codigo_mais_alto,peso_mais_alto

def mais_baixo(codigos,alturas,pesos):
    alunos_mais_baixo = alturas[0]
    codigo_mais_baixo = codigos[0]
    peso_mais_baixo = pesos[0]
    for i in range(len(alturas)):
        if alturas[i] < alunos_mais_baixo:
            alunos_mais_baixo = alturas[i]
            codigo_mais_baixo = codigos[i]
            peso_mais_baixo = pesos[i]
    return alunos_mais_baixo,codigo_mais_baixo,peso_mais_baixo

def mais_gordo(codigos,alturas,pesos):
    aluno_mais_gordo = pesos[0]
    codigo_mais_gordo = codigos[0]
    altura_mais_gordo = alturas[0]
    for i in range(len(pesos)):
        if pesos[i] > aluno_mais_gordo:
            aluno_mais_gordo = pesos[i]
            codigo_mais_gordo = codigos[i]
            altura_mais_gordo = alturas[i]
    return aluno_mais_gordo,codigo_mais_gordo,altura_mais_gordo

def mais_magro(codigos,alturas,pesos):
    aluno_mais_magro = pesos[0]
    codigo_mais_magro = codigos[0]
    altura_mais_magro = alturas[0]
    for i in range(len(pesos)):
        if pesos[i] < aluno_mais_magro:
            aluno_mais_magro = pesos[i]
            codigo_mais_magro = codigos[i]
            altura_mais_magro = alturas[i]
    return aluno_mais_magro,codigo_mais_magro,altura_mais_magro


def media_pesos_alturas(pesos,alturas):
    media = sum(alturas)/ len(alturas)
    mediap = sum(pesos)/ len(pesos)
    return media, mediap
            
def main():
    codigos = []
    alturas = []
    pesos = []
    while True:
        codigo = int(input('Digite o seu código: '))
        if codigo == 0:
            break
        else:
            codigos.append(codigo)
        altura = float(input('A sua altura: ' ))
        alturas.append(altura)
        peso = float(input('O seu peso: '))
        pesos.append(peso)
        
    #chamar as funções
    alunos_mais_alto,codigo_mais_alto,peso_mais_alto = mais_alto(codigos,alturas,pesos)
    alunos_mais_baixo,codigo_mais_baixo,peso_mais_baixo = mais_baixo(codigos,alturas,pesos)
    aluno_mais_gordo,codigo_mais_gordo,altura_mais_gordo = mais_gordo(codigos,alturas,pesos)
    aluno_mais_magro,codigo_mais_magro,altura_mais_magro = mais_magro(codigos,alturas,pesos)
    media, mediap = media_pesos_alturas(pesos,alturas)
    
    print(f'{codigos}\n{alturas}\n{pesos}')
    print(f'O aluno mais alto é {alunos_mais_alto:.2f}m com código {codigo_mais_alto} com peso {peso_mais_alto:.2f}gg.')
    print(f'O aluno mais baixo é {alunos_mais_baixo:.2f}m com código {codigo_mais_baixo} com peso {peso_mais_baixo:.2f}kg.')
    print(f'O aluno mais gordo é {aluno_mais_gordo:.2f}kg com código {codigo_mais_gordo} com altura de {altura_mais_gordo:.2f}m.')
    print(f'O aluno mais magro é {aluno_mais_magro:.2f}kg com código {codigo_mais_magro} com altura de {altura_mais_magro:.2f}m')
    print(f'Á média de altura e pesos é {media:.2f}m e {mediap:.2f}kg respectivamentes.')


if __name__ == '__main__':
    main()