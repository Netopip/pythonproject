import datetime
def ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 !=0) or ano % 400 == 0:
        return 'É bissexto'
    else:
        return 'Não é bissexto'
#Um ano é bissexto se for divisível por 4.
#No entanto, anos divisíveis por 100 não são bissextos, a menos que também sejam divisíveis por 400.
#Assim, a expressão (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) cobre todas as regras corretamente.
def main():
    ano = int(input('Digite o ano a ser analisado: [1 para ano atual] '))
    if ano == 1:
        ano = datetime.date.today().year
    msg = ano_bissexto(ano)
    print(f'O ano de {ano} {msg}.')

if __name__ == '__main__':
    main()