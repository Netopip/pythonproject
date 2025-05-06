def verificar_numero(numero):
    if numero % 2 == 0:
        paridade = 'par'
    else:
        paridade = 'Impár'

    if numero > 0:
        sinal = 'positivo'
    elif numero < 0:
        sinal = 'negativo'
    else:
        sinal = 'neutro'

    if numero == int(numero):
        tipo = 'inteiro'
    else:
        tipo = 'decimal'

    return paridade,sinal,tipo

def realizar_operacao(num1,num2, operacao):
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1/num2
        else:
            return 'Erro: Divisão por zero.'
    else:
        return 'Operaçaõ invalida'

    paridade,sinal,tipo = verificar_numero(resultado)

    return f'O resultado da operação é {resultado:.2f}.\n'\
           f'Este numero é {paridade}, {sinal} e {tipo}.'

def main():
    try:
        num1 = float(input('Digite o primeiro numero: '))
        num2 = float(input('Digte o segundo numero: '))
        operacao = input('Escolha a operação : (+,-,*,/): ')
        resultado = realizar_operacao(num1,num2,operacao)
        print(resultado)
    except ValueError:
        print('Entrada invalida. Por favor, digte numeros validos.')

if __name__ == '__main__':
    main()