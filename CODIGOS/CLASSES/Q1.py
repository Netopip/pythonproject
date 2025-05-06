'''Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor'''

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        
    def trocarCor(self, nova_cor):
        self.cor = nova_cor
        
    def mostrarCor(self):
        return self.cor
    
bola1 = Bola('Azul', 25, 'Couro')
print(bola1.mostrarCor())  # Saída: Azul


