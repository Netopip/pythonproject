'''Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.'''
def converter_horas(hora,minutos):
    lista_horas_conversao = [1,2,3,4,5,6,7,8,9,10,11]
    lista_hora_real = [13,14,15,16,17,18,19,20,21,22,23]
    _min = minutos 
    
    for i,j in enumerate(lista_hora_real):
        if hora == j:
            print(f'O horario convertido é {lista_horas_conversao[i]}:{_min} PM')
        elif hora == 12:
            print(f'O horario é {12}:{_min} PM')
            break
        elif hora == 24:
            print(f'O horario convertido é {00}:{_min} AM')
            break
    
    

def main():
    while True:
        entrada1 = str(input('Digite as horas:\n').strip())
        entrada2 = str(input('Digite os minutos:\n').strip())
        try:
            hora = int(entrada1)
            minutos = int(entrada2)
            if hora < 0 or hora > 24 or minutos < 0 or minutos > 59:
                print('Horario inválido.')
            elif hora < 12 and minutos > 0 and minutos < 59:
                print(f'O horário é {hora}:{minutos} AM')
            else:
                converter_horas(hora,minutos)
                 
        except ValueError:
            print('Entrada inválida.')
        
        opcao = str(input('Quer continuar? (sim para continuar// não para parar)\n').strip()).upper()
        if opcao != 'SIM':
            break
    print('Até mais!')
    
    
if __name__ == '__main__':
    main()
            
            
        