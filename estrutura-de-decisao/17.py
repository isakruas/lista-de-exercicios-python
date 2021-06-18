"""
17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se
este ano é ou não bissexto
"""
from datetime import datetime, timedelta

ano = abs(int(input('Informe um ano\n')))
ano = datetime(ano, 2, 28) + timedelta(days=1)
if ano.month == 2:
    print(f'O ano {ano.year} é bissexto\n')
else:
    print(f'O ano {ano.year} não bissexto\n')
