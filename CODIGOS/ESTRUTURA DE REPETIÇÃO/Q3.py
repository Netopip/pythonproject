def main():
    while True:
        nome = str(input())
        idade = int(input())
        salario = float(input())
        sexo = str(input()).lower()
        estado_civil = str(input())
        if len(nome) < 3:
            print('Nome invalido!')
            continue
        elif not (0 <= idade <= 150):
            print('Idade invalida!')
            continue
        elif salario <= 0:
            print('Salario invalido!')
            continue
        elif sexo not in 'fm':
            print('Sexo invalido')
            continue
        elif estado_civil not in 'scvd':
            print('Estado civil invalido!')
            continue
        else:
            print('Todos os dados válidos')
            return nome,idade,salario,sexo,estado_civil

if __name__ == '__main__':
    main()