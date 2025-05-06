'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''
import math
area = float(input('Quantos M² você quer pintar: '))
litros = area / 3
latas = math.ceil(litros / 18)#a função ceil aproxima o numero de ponto flutuante para cima(mais)
custo = math.ceil(latas * 80)
print(f'A quantidade de latas a serem compradas para cobrir a area de {area}m² é de {latas} latas\nE o custo total é de R${custo}')
