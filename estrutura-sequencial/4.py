"""
4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
from statistics import mean


numeros = input('Informe quatro números (ou mais) separados por espaço\n')
numeros = numeros.split()
numeros = [int(numero) for numero in numeros]
print(f'A media dos numeros é: {mean(numeros)}\n')
