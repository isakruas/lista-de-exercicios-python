"""
28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
    porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
    receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de
    carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de
    carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""
desconto = 0
__tipo_de_carne = {
    '1': {
        'nome': 'File Duplo',
        'v<=5': 4.9,
        'v>5': 5.8
    },
    '2': {
        'nome': 'Alcatra',
        'v<=5': 5.9,
        'v>5': 6.8
    },
    '3': {
        'nome': 'Picanha',
        'v<=5': 6.9,
        'v>5': 7.8
    }
}
__tipo_de_pagamento = {
    '1': 'Cartão Tabajara',
    '2': 'Outro'
}
tipo_de_carne = input('[1] - File Duplo\n[2] - Alcatra\n[3] - Picanha\n')
quantidade_de_carne = abs(int(input('Qual a quantidade de carne (em Kg)\n')))
tipo_de_pagamento = input('[1] - Cartão Tabajara\n[2] - Outro\n')
if tipo_de_pagamento == '1':
    desconto = 0.05
if 0 < quantidade_de_carne <= 5:
    preco_total = quantidade_de_carne * __tipo_de_carne[tipo_de_carne]['v<=5']
else:
    preco_total = quantidade_de_carne * __tipo_de_carne[tipo_de_carne]['v>5']
print(f"""
    ------------------------------------------------------
    -                Cupom Fiscal                        -
    ------------------------------------------------------
    - Tipo de carne         : {__tipo_de_carne[tipo_de_carne]['nome']}
    - Quantidade de carne   : {quantidade_de_carne} Kg
    - Preço total           : R$ {round(preco_total, 2)}
    - Tipo de pagamento     : {__tipo_de_pagamento[tipo_de_pagamento]}
    - Valor do desconto     : R$ {round(preco_total  * desconto, 2)}
    - Valor a pagar         : R$ {round(preco_total * (1 - desconto), 2)}
    ------------------------------------------------------
""")
