numero = int(input('Digite um número inteiro: '))
cont = 0

for i in range(1,numero + 1):
    if numero % i == 0:
        cont += 1
if cont == 2:
    print('É primo.')
else:
    print('Não é primo')