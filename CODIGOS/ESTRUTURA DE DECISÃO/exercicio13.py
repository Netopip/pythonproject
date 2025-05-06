def dia_corre(num):
    if num == 1:
        return 'DOMINGO'
    if num == 2:
        return 'SEGUNDA'
    if num == 3:
        return 'TERÇA'
    if num == 4:
        return 'QUARTA'
    if num == 5:
        return 'QUINTA'
    if num == 6:
        return 'SEXTA'
    if num == 7:
        return 'SÁBADO'
    else:
        return 'VALOR INVÁLIDO'




def main():
    numero = int(input('Digite um numero correspondente ao dia da semana: '))

    msg = dia_corre(numero)
    print(msg)

if __name__ == '__main__':
    main()
