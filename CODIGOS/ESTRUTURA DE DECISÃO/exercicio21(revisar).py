def caixa_eletronico():
    valor_saque = int(input("Digite o valor que deseja sacar (entre 10 e 600 reais): "))

    if valor_saque < 10 or valor_saque > 600:
        print("Valor inválido para saque. O valor mínimo é 10 reais e o máximo é 600 reais.")
        return

    # Definindo as notas disponíveis
    notas = [100, 50, 10, 5, 1]
    qtd_notas = [0, 0, 0, 0, 0]  # Para armazenar a quantidade de cada nota

    # Calculando a quantidade de cada nota
    for i in range(len(notas)):
        while valor_saque >= notas[i]:
            qtd_notas[i] += 1
            valor_saque -= notas[i]

    # Exibindo o resultado
    print("Notas fornecidas:")
    for i in range(len(notas)):
        if qtd_notas[i] > 0:
            print(f"{qtd_notas[i]} nota(s) de {notas[i]} reais")


# Executando o programa
caixa_eletronico()

