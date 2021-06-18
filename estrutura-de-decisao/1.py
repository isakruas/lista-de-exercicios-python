"""
1. Faça um Programa que peça dois números e imprima o maior deles.
"""

numeros = set()
while True:
    try:
        numero = int(input(f'Informe o {len(numeros)+1}º número\n'))
        numeros.add(numero)
        if len(numeros) == 2:
            break
        pass
    except ValueError:
        pass
print(f'O maior número informedo foi {max(numeros)}')
