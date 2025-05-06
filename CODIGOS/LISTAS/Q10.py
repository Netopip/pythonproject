'''Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.'''

def vetor_C(vetor1,vetor2):
    vetor_c = []
    
    for i in range(len(vetor1)):
        vetor_c.append(vetor1[i])
        vetor_c.append(vetor2[i])
    print(vetor_c)
        
def main():
    vetor1 = []
    vetor2 = []
    
    for i in range(10):
        number = int(input())
        vetor1.append(number)
        
    for j in range(10):
        number2 = int(input())
        vetor2.append(number2)
        
    vetor_C(vetor1,vetor2)
    
if __name__ == '__main__':
    main()