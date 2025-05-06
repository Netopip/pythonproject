def exponeciacao(base,expoente):
    resultado = 1
    for i in range(abs(expoente)):
        resultado *= base
    if expoente < 0:
        resultado = 1/resultado
    return resultado      



def main():
    base = int(input('Base: '))
    expoente = int(input('Expoente: '))
    
    resultado = exponeciacao(base, expoente)
    print(f'O resultado é {resultado}')

if __name__== '__main__':
    main()        