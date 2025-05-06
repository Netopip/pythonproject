
def main():
    while True:
        usuario = str(input('Digite seu nome de usuário: '))
        senha = str(input('Digite sua senha: '))
        if usuario != senha:
            print('Usuario e senhas validas!')
            break
        else:
            print('Erro. O usuairo não pode ser igual a senha!')

    print('Fim')

if __name__ == '__main__':
    main()