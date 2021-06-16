"""
14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São
Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que
leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do
limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens
adequadas.
"""

limite_de_peso = 50


def calcule_o_excesso(peso):
    """
    Calcular o excesso de pesso dos peixes
    :param peso: Peso dos peixes capturados
    :return:  Peso de peixes que exede o limite
    >>> calcule_o_excesso(60)
    10
    >>> calcule_o_excesso(50)
    0
    >>> calcule_o_excesso(40)
    0
    """
    global limite_de_peso
    if peso > limite_de_peso:
        return peso - limite_de_peso
    else:
        return 0


peso_de_peixes = float(input('Informe o peso de peixes\n'))
excesso_de_peso = calcule_o_excesso(peso_de_peixes)

multa_por_quilo = 4
multa = multa_por_quilo*excesso_de_peso

print(f'Peso de peixes: {peso_de_peixes}\nLimite de peso: {limite_de_peso}\nQuantidade de quilos além do limite: '
      f'{excesso_de_peso}\nMulta por quilo de peixe em excesso: {multa_por_quilo}\nValor da multa: {multa}')
