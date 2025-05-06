def decompor_numero(numero):
    if numero >= 1000 or numero <= 0:
        print("O número deve ser menor que 1000 e maior que zero.")
        return

    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    partes = []  # Uma lista é criada para colocar os valores da centena, dezena e unidade.

    if centenas > 0:
        if centenas == 1:
            partes.append(f"{centenas} centena")
        else:
            partes.append(f"{centenas} centenas")

    if dezenas > 0:
        if dezenas == 1:
            partes.append(f"{dezenas} dezena")
        else:
            partes.append(f"{dezenas} dezenas")

    if unidades > 0:
        if unidades == 1:
            partes.append(f"{unidades} unidade")
        else:
            partes.append(f"{unidades} unidades")

    if partes:
        if len(partes) > 1:
            resultado = ", ".join(partes[:-1]) + " e " + partes[-1] #partes[:-1] seleciona todos os elementos da lista, exceto o último.|", ".join(partes[:-1]) junta todos esses elementos em uma única string, separando-os por vírgulas.
                                                                    #partes[-1] é o último elemento da lista.
        else:
            resultado = partes[0]
        print(f'O número {numero} contém: {resultado}.')
    else:
        print("O número é zero e não contém centenas, dezenas ou unidades.")

# Leitura do número
numero = int(input("Digite um número inteiro menor que 1000 e maior que zero: "))
decompor_numero(numero)
