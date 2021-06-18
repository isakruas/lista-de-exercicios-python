"""
23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.
"""
numero = input('Informe um número\n')
if (float(numero) * 10) % 10 != 0:
    print('É decimal\n')
else:
    print('É inteiro')
