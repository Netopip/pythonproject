resposta_sim = list()

pergunta1 = str(input('Telefonou para a vitima? ')).lower().strip()
if pergunta1 == 'sim':
    resposta_sim.append(1)
else:
    resposta_sim.append(0)
pergunta2 = str(input('Esteve no local do crime? ')).lower().strip()
if pergunta2 == 'sim':
    resposta_sim.append(1)
else:
    resposta_sim.append(0)
pergunta3 = str(input('Mora perto da vítima? ')).lower().strip()
if pergunta3 == 'sim':
    resposta_sim.append(1)
else:
    resposta_sim.append(0)
pergunta4 = str(input('Devia para a vítima? ')).lower().strip()
if pergunta4 == 'sim':
    resposta_sim.append(1)
else:
    resposta_sim.append(0)
pergunta5 = str(input('Ja trabalhu com a vitima? ')).lower().strip()
if pergunta5 == 'sim':
    resposta_sim.append(1)
else:
    resposta_sim.append(0)

if sum(resposta_sim) == 2:
    print('Você é considerado Suspeito')
elif sum(resposta_sim) == 3 or sum(resposta_sim) == 4:
    print('Você é considerado Cumplice')
elif sum(resposta_sim) == 5:
    print('Você é considerado Culpado')
