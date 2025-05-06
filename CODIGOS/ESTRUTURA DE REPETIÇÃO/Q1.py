def retornar_nota():
    while True:
        nota = float(input('Digite uma nota entre 0 a 10: '))
        if 0<= nota <=10:
            return nota
        else:
            print('Nota inválida, tente novamente"')


def main():

    resultado = retornar_nota()
    print(f'A nota é {resultado}')

if __name__ == '__main__':
    main()