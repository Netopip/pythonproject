def preco(precos):
    menor = min(precos)
    indice = precos.index(menor)# o 1 adicionado poderia ser aqui!
    return menor, indice + 1

def main():
    produto1 = float(input())
    produto2 = float(input())
    produto3 = float(input())

    precos = [produto1, produto2, produto3]
    menor, indice = preco(precos)
    print (f'O menor valor entre os, R${produto1}, R${produto2} e R${produto3} é o R${menor} que corresponde ao produto {indice}.')

if __name__ == '__main__':
    main()