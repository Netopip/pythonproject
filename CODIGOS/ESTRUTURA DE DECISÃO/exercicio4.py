tecla= str(input('Digite uma tecla: ')).upper()
if tecla in 'AEIOU':
    print(f'A tecla {tecla} é uma vogal.')
elif tecla.isnumeric():
    print(f'A tecla {tecla} é um numero.')
elif tecla == ' ':
    print(f'A tecla {tecla} é o espaço.')
elif tecla in 'BCDFGHJKLMNPQRSTVWXYZ':
    print(f'A tecla {tecla} é uma consoante.')
else:
    print(f'A tecla {tecla} é um simbolo.')