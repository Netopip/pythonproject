
def main():
    cont_par = 0
    cont_impar = 0
    for i in range(1,11):
        numero = int(input('Digite um numero inteiro: '))
        if numero % 2 == 0:
            cont_par += 1
        else:
            cont_impar += 1
    print(f'O quantidade de números impar digita foi "{cont_impar}".')
    print(f'O quantidade de números par digita foi "{cont_par}".')

if __name__ == '__main__':
    main()
