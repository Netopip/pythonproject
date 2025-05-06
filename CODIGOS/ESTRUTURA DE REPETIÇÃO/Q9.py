
def main():
    lista= list()
    for i in range(1,51):
        if i % 2 != 0:
            lista.append(i)
        else:
            continue
    print(f'Segue a lista dos numero impares no intervalo de (1 a 50):\n{lista}.\nUm total de {len(lista)} numeros.')


if __name__ == '__main__':
    main()
