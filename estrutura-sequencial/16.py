"""
16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
preço total
"""
metros_quadrados = float(input('Qual o tamanho em metros quadrados da área a ser pintada?\n'))
litros_de_tinta_nescessarios = round(metros_quadrados / 3, 2)


def quantidades_de_latas(litros_de_tinta):
    """
    Calcula a quantidade de lastas pra a quantidade de litros de tinta dados
    :param litros_de_tinta:
    :return: quantidade de latas de tinta
    >>> quantidades_de_latas(17)
    1
    >>> quantidades_de_latas(18)
    1
    >>> quantidades_de_latas(36)
    2
    >>> quantidades_de_latas(35)
    2
    >>> quantidades_de_latas(37)
    3
    """
    if litros_de_tinta <= 18:
        return 1
    else:
        latas = str(round(litros_de_tinta / 18, 1)).split('.')
        if latas[1] != '0':
            return int(latas[0]) + 1
        return int(latas[0])


print(f"""
Será nescessário comprar {quantidades_de_latas(litros_de_tinta_nescessarios)} lata de tintas\n
O valor total será R$ {quantidades_de_latas(litros_de_tinta_nescessarios) * 80}
""")
