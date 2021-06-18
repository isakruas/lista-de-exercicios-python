"""
26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro

    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro

    Escreva um algoritmo que leia o número de litros vendidos, o tipo de
    combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
    sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""
while True:
    print('-' * 30)
    combustivel = input('[A] - álcool\n[G] - gasolina\n')
    if len(combustivel) == 0:
        pass
    combustivel = combustivel[0].upper()
    if combustivel not in 'AG':
        pass
    else:
        try:
            litros = abs(float(input('Número de litros vendidos\n')))
            if combustivel == 'G':
                preco = 2.5
                if litros <= 20:
                    preco = preco * (1 - 0.04)
                elif litros > 20:
                    preco = preco * (1 - 0.06)
                print(f'O valor a ser pago pelo cliente é R$ {round(litros * preco, 2)}')
            if combustivel == 'A':
                preco = 1.9
                if litros <= 20:
                    preco = preco * (1 - 0.03)
                elif litros > 20:
                    preco = preco * (1 - 0.05)
                print(f'O valor a ser pago pelo cliente é R$ {round(litros * preco, 2)}')
            pass
        except ValueError:
            pass
