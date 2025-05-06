def main():
    cand1 = 0
    cand2 = 0
    cand3 = 0
    eleitores = int(input('Total de eleitores:'))
    for i in range(eleitores):
        voto = int(input('Qual o seu voto :\nCANDIDATO 1: 1 \nCANDIDATO 2: 2\nCANDIDATO 3: 3'))
        if voto == 1:
            cand1 += 1
        elif voto == 2:
            cand2 += 1
        elif voto == 3:
            cand3 += 1
        else:
            print('Opção inválida.')
    print(f'A quantidades de votos do \ncandidato 1 é {cand1}\ncandidato 2 é {cand2}\ncandidato 3 é {cand3}')
            
if __name__ == '__main__':
    main()
        