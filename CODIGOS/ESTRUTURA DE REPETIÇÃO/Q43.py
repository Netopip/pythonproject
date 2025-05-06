'''O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.'''

def main():
    
    total_pagar = 0
    while True:
        print('ESPECIFICAÇÃO    CÓDIGO      PREÇO\n'
              'Cachorro quente   100         R$ 1,20\n'
              'Bauru simples     101         R$ 1,30\n'
              'Bauro c/ ovo      102         R$ 1,50\n'
              'Hamburguer        103         R$ 1,20\n'
              'Cheeseburguer     104         R$ 1,30\n'
              'Refrigerante      105         R$ 1,00\n'
                      'Insira 0 para encerrar')
        opcao = int(input('Digite o código do produto para adicionar a compra: ').strip())
        if opcao == 100:
            total_pagar += 1.20
        elif opcao == 101:
            total_pagar += 1.30
        elif opcao == 102:
            total_pagar += 1.50
        elif opcao == 103:
            total_pagar += 1.20
        elif opcao == 104:
            total_pagar += 1.30
        elif opcao == 105:
            total_pagar += 1
        elif opcao == 0:
            break
        else:
            print('DIGITE UM CÓDIGO VÁLIDO!')
    
    print(f'O total a pagar é de R$ {total_pagar:.2f}!')
        
    
if __name__ == '__main__':
    main()
                        
