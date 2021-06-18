"""
8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""
precos = set()
print('Informe preço de três produtos\n')
while True:
    try:
        preco = float(input(f'    - produto {len(precos)+1}, preço:\n    '))
        precos.add(preco)
        if len(precos) == 3:
            break
        pass
    except ValueError:
        pass
print(f'Você devetrá comprar o produto, cujo preço é {min(precos)}\n')
