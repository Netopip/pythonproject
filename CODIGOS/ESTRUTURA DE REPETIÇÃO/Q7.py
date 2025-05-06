def definir_maior():
    maior = 0
    for i in range(5):
        numero = int(input('Digite um numero: '))
        if numero > maior:
            maior = numero
    return maior


def main():
    resultado = definir_maior()

    print(f"O maior numero dos lidos é o {resultado}")

if __name__ == '__main__':
    main()
