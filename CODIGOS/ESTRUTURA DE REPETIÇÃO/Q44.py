'''Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.'''

def porcentagem_nulos(cont_votos, votos_nulo):
    por_nulo = (votos_nulo/cont_votos) * 100
    return round(por_nulo,2)

def porcentagem_brancos(votos_brancos, cont_votos):
    por_branco = (votos_brancos/cont_votos) * 100
    return round(por_branco,2)
    

def main():
    
    cont_votos = 0
    votos_neto = 0
    votos_vitorio = 0
    votos_jonas = 0
    votos_vini = 0
    votos_nulo = 0
    votos_brancos = 0
    
    while True:
        print('CÓDIGO       CANDIDATO       \n'
            '1             NETO\n'
            '2             VITÓRIO\n'
            '3             JONAS\n'
            '4             VINICIUS\n'
            '5             VOTO NULO\n'
            '6             VOTO EM BRANCO')
        
        voto = int(input('Digite o seu voto: ').strip())
        if voto == 1:
            cont_votos += 1
            votos_neto += 1
        elif voto == 2:
            cont_votos += 1
            votos_vitorio += 1
        elif voto == 3:
            cont_votos += 1
            votos_jonas += 1
        elif voto == 4:
            cont_votos += 1
            votos_vini += 1
        elif voto == 5:
            cont_votos += 1
            votos_nulo += 1
        elif voto == 6:
            cont_votos += 1
            votos_brancos += 1
        elif voto == 0:
            break
        else:
            print('Código inválido!')
            
    por_nulo = porcentagem_nulos(cont_votos, votos_nulo)
    por_branco = porcentagem_brancos(votos_brancos, cont_votos)
            
    print(f'Total de votos {cont_votos}: Neto {votos_neto} || Vitorio {votos_vitorio} || Jonas {votos_jonas} || Vinicius {votos_vini}  || Nulo {votos_nulo}  || Brancos {votos_brancos}')
    print(f'Porcentagem de votos nulos {por_nulo}\nPorcentagem de votos brancos {por_branco}')
    
    
    
if __name__ == '__main__':
    main()