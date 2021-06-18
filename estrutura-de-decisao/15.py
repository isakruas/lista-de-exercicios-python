"""
15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
"""


def lados():
    """
    Coleta os lados no terminal
    :return: Lista com os lados
    """
    __lados = list()
    while True:
        try:
            lado = float(input(f'Informe a {len(__lados) + 1}º lado\n'))
            __lados.append(lado)
            if len(__lados) == 3:
                break
            pass
        except ValueError:
            pass
    if (__lados[0] + __lados[1]) > __lados[2]:
        return __lados
    else:
        print('Os valores não podem formar um triângulo\n')
        return lados()


a, b, c = lados()
if a == b == c:
    print('Triângulo Equilátero: três lados iguais\n')
elif a == b or a == c:
    print('Triângulo Isósceles: quaisquer dois lados iguais\n')
else:
    print('Triângulo Escaleno: três lados diferentes\n')
