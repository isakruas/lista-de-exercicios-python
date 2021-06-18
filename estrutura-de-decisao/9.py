"""
9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
numeros = set()
while True:
    try:
        numero = int(input(f'Informe o {len(numeros)+1}º número\n'))
        numeros.add(numero)
        if len(numeros) == 3:
            break
        pass
    except ValueError:
        pass

print(list(numeros)[::-1])
