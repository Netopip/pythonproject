def turno(letra):
    if letra == 'M':
        return 'Bom dia!'
    elif letra == 'V':
        return  'Boa tarde!'
    elif letra == 'N':
        return  'Boa noite!'
    else:
        return 'Valor Invalido'

def main():
    msg = str(input('Digite: [M,V,N] ')).strip().upper()

    resposta = turno(msg)
    print(resposta)

if __name__ == '__main__':
    main()