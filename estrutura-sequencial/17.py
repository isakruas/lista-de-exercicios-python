"""
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as
quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
os valores para cima, isto é, considere latas cheias.
"""


def quantidades_de_latas(litros_de_tinta, __litros_por_galoes=18.0, misturar=False):
    """
    Calcula a quantidade de lastas pra a quantidade de litros de tinta dados
    :param misturar: Define se deve otimizar ou não
    :param __litros_por_galoes: Capacidade do galão de tinta
    :param litros_de_tinta: litros de tintas nescessarios
    :return: quantidade de latas de tinta grandes, pequenas ou (latas_grandes, latas_pequenas)

    comprar apenas latas de 18 litros

    >>> quantidades_de_latas(17)
    1
    >>> quantidades_de_latas(18)
    1
    >>> quantidades_de_latas(32.4)
    2
    >>> quantidades_de_latas(30)
    2
    >>> quantidades_de_latas(45)
    3

    comprar apenas galões de 3,6 litros

    >>> quantidades_de_latas(3.6, 3.6)
    1
    >>> quantidades_de_latas(3.5, 3.6)
    1
    >>> quantidades_de_latas(6.1, 3.6)
    2
    >>> quantidades_de_latas(6.48, 3.6)
    2
    >>> quantidades_de_latas(10.3, 3.6)
    3

    misturar latas e galões

    >>> quantidades_de_latas(21.6, misturar=True)
    (1, 1)

    >>> quantidades_de_latas(115.2, misturar=True)
    (6, 2)

    >>> quantidades_de_latas(17, misturar=True)
    (1, 0)
    >>> quantidades_de_latas(20, misturar=True)
    (1, 1)
    """

    litros_por_galoes = lambda x: {'18.0': 18.0, '3.6': 3.6}.get(x)
    litros_por_galoes = litros_por_galoes(str(__litros_por_galoes))

    if not misturar:
        if litros_de_tinta <= litros_por_galoes:
            return 1
        else:
            latas = int(round((litros_de_tinta / litros_por_galoes) * 1.1, 0))
            return latas

    lata_grande = int(round((litros_de_tinta / 18) * 1.1, 0))

    while True:

        litros_de_tinta_restantes = litros_de_tinta - lata_grande * 18
        lata_pequena = int(round((litros_de_tinta_restantes / 3.6) * 1.1, 0))
        if lata_grande >= 0 and lata_pequena >= 0:
            return lata_grande, lata_pequena
        else:
            lata_grande -= 1
            pass


metros_quadrados = float(input('Qual o tamanho em metros quadrados da área a ser pintada?\n'))
litros_de_tinta_nescessarios = round(metros_quadrados / 6, 2)
lata_grande = quantidades_de_latas(litros_de_tinta_nescessarios)
lata_pequena = quantidades_de_latas(litros_de_tinta_nescessarios, 3.6)
lata_grande_e_lata_pequena = quantidades_de_latas(litros_de_tinta_nescessarios, misturar=True)
print(f"""
Você pode comprar {lata_grande} latas de 18 litros; pagando R$ {lata_grande*80},
ou comprar {lata_pequena} galões de 3,6 litros; pagando R$ {lata_pequena*25},
ou misturar e comprar {lata_grande_e_lata_pequena[0]} latas e {lata_grande_e_lata_pequena[1]} galões; pagando R$ \
{lata_grande_e_lata_pequena[0]*80+lata_grande_e_lata_pequena[1]*25} 
""")
