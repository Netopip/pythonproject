'''Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.'''

def retornar_soma(a,b,c):
    soma = a + b + c
    return soma

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    
    soma = retornar_soma(n1,n2,n3)
    print(soma)
            
if __name__ == '__main__':
    main()
        