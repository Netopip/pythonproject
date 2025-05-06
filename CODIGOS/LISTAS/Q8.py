'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.'''

def ordem_inversa(vetor):
    for pessoa in reversed(vetor):
        print(pessoa)
        
def main():
    vetor = []
    
    for i in range(5):
        idade = int(input('Digite a sua idade: ').strip())
        altura = float(input('Adicione a sua altura:(em metros) ').strip())
        vetor.append([idade,altura])
    
    ordem_inversa(vetor)
        
if __name__ == '__main__':
    main()