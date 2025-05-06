'''Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.'''

def vetor_C(vetor1,vetor2,vetor3):
    vetor_c = []
    
    for i in range(len(vetor1)):
        vetor_c.append(vetor1[i])
        vetor_c.append(vetor2[i])
        vetor_c.append(vetor3[i])
    print(vetor_c)
        
def main():
    vetor1 = []
    vetor2 = []
    vetor3 = []
    
    for i in range(10):
        number = int(input())
        vetor1.append(number)
        
    for j in range(10):
        number2 = int(input())
        vetor2.append(number2)
    
    for k in range(10):
        number3 = int(input())
        vetor3.append(number3)
        
    vetor_C(vetor1,vetor2,vetor3)
    
if __name__ == '__main__':
    main()