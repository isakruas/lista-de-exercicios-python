"""
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a. o produto do dobro do primeiro com metade do segundo.
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo.
"""
numeros = input('Informe 3 números separados por espaço,\nsendo 2 primeiros inteiros e um número real\n')
numeros = numeros.split()
primeiro_numero = int(numeros[0])
segundo_numero = int(numeros[1])
terceiro_numero = float(numeros[2])
a = round((2*primeiro_numero)*(segundo_numero/2), 2)
b = round(3*primeiro_numero+terceiro_numero, 2)
c = round(terceiro_numero**3, 2)
print(f'O produto do dobro do primeiro com metade do segundo {a}')
print(f'A soma do triplo do primeiro com o terceiro {b}')
print(f'O terceiro elevado ao cubo {c}')
