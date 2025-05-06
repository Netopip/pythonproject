def calcular_valor(tipo, litros):
    alcool = 1.90
    gasolina = 2.50

    if tipo == 'A':
        if litros <= 20:
            desconto = 0.03
        else:
            desconto = 0.05
        preco = alcool
    elif tipo == 'G':
        if litros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06
        preco = gasolina
    else:
        return 'Tipo de combustivel invalido'
    valor_sem_desconto = litros * preco
    valor_com_desconto = valor_sem_desconto * desconto
    valor_final = valor_sem_desconto - valor_com_desconto
    return valor_final



def main():
    tipo = str(input('Digite "A" para alcool e "G" para gasolina: ')).strip().upper()
    litros  = float(input('Digite a quantidade de litros: '))

    valor_pagar = calcular_valor(tipo,litros)

    print(f'{valor_pagar:.2f}')

if __name__ == '__main__':
    main()




