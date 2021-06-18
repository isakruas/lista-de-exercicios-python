"""
21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O
valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5
    e uma nota de 1;

    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de
    50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""


def saque(valor):
    """
    Informar quantas notas de cada valor serão fornecidas
    :param valor:
    :return: Dicionários contendo a quantidade de notas para cada valor
    >>> notas(256)
    {'100': 2, '50': 1, '10': 0, '5': 1, '1': 1}
    >>> notas(399)
    {'100': 3, '50': 1, '10': 4, '5': 1, '1': 4}
    """
    __notas = dict()
    __notas['100'] = valor // 100
    __notas['50'] = (valor - 100 * __notas['100']) // 50
    __notas['10'] = (valor - (100 * __notas['100'] + 50 * __notas['50'])) // 10
    __notas['5'] = (valor - (100 * __notas['100'] + 50 * __notas['50'] + 10 * __notas['10'])) // 5
    __notas['1'] = (valor - (100 * __notas['100'] + 50 * __notas['50'] + 10 * __notas['10'] + 5 * __notas['5'])) // 1
    return __notas


valor_do_saque = abs(int(input('Qual o valor do saque?\n')))

if not 10 <= valor_do_saque <= 600:
    print('O valor mínimo é de 10 reais e o máximo de 600 reais\n')
    exit(0)

notas = saque(valor_do_saque)

print(f"""
Serão fornecidas:
    {notas['100']} notas de 100
    {notas['50']} notas de 50
    {notas['10']} notas de 10
    {notas['5']} notas de 5
    {notas['1']} notas de 1
""")
