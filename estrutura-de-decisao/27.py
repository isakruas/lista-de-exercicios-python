"""
27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
    desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (
    em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""
morango = abs(int(input('Qual a quantidade (em Kg) de morangos?\n')))
maca = abs(int(input('Qual a quantidade (em Kg) de maças?\n')))
valor_morango = None
valor_maca = None
desconto = 0
if morango > 5:
    valor_morango = morango * 2.2
else:
    valor_morango = morango * 2.5
if maca > 5:
    valor_maca = maca * 1.5
else:
    valor_maca = maca * 1.8
if maca + morango > 8 or maca * valor_maca + morango * valor_morango > 25:
    desconto = 0.1
print(f'O escreva o valor a ser pago pelo cliente é de R$ {round((valor_maca + valor_morango) * (1 - desconto), 2)}')
