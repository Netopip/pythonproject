'''Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;'''


class Quadrado:
    def __init__(self,lado):
        self.lado = lado
        
    def mudarLado(self, novo_lado):
        self.lado = novo_lado
    
    def retornarLado(self):
        return self.lado    
        
    def areaQuadrado(self):
        area = self.lado ** 2
        return area

def main():
    while True:
        entrada = str(input('Digite o valor do lado do quadrado:\n'))
        try:
            lado = int(entrada)
            if lado <= 0:
                print('O valor do lado do quadrado não pode ser menor ou igual a zero.')
            else:
                quadrado = Quadrado(lado)
                print(f'A área do quadrado de lado {quadrado.retornarLado()} é : {quadrado.areaQuadrado()}')
                break
                
        except ValueError:
            print('Entrada inválida!')
        
if __name__ == '__main__':
    main()
        