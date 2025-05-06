'''O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.''' 

def maior_menor_temp(temperaturas):
    maior = max(temperaturas)
    menor = min(temperaturas)
    return maior, menor

def media_temp(temperaturas):
    media = sum(temperaturas)/len(temperaturas)
    return media

def main():
    temperaturas = []
    while True:
        temp = float(input())
        if temp == 999:
            break
        temperaturas.append(temp)

    maior, menor = maior_menor_temp(temperaturas)
    media = media_temp(temperaturas)
    print(f'A maior temperatura registrada foi {maior}\nA menor temperatura é {menor}\nE a média das temperaturas foi de {media}.')
    
    
if __name__ == '__main__':
    main()