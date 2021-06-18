"""
12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e
que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário
o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o
    exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00
"""


def folha_de_pagamento(__salario):
    """

    :param __salario: salário bruto
    :return: cálculo da folha de pagamento [IR, INSS, FGTS, Total de descontos, Salário Liquido]

    >>> folha_de_pagamento(1100)
    [55.0, 110.0, 121.0, 165.0, 935.0]
    """
    ir = []
    inss = 0.10
    fgts = 0.11
    desconto = 0
    if 0 <= __salario <= 900:
        desconto = 0
    elif 900 < __salario <= 1500:
        desconto = 0.05
    elif 1500 < __salario <= 2500:
        desconto = 0.10
    elif __salario >= 2500:
        desconto = 0.20
    ir.append(desconto * __salario)
    ir.append(inss * __salario)
    ir.append(fgts * __salario)
    ir.append(ir.__getitem__(0) + ir.__getitem__(1))
    ir.append(__salario - (ir.__getitem__(0) + ir.__getitem__(1)))
    return ir


valor_da_hora = float(input('Informe o valor da sua hora\n'))
horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas no mês\n'))
salario = valor_da_hora * horas_trabalhadas
calculo = folha_de_pagamento(salario)
print(calculo)
print(f"""
            Salário Bruto:                  : R$ {salario}
            (-) IR ({int((calculo[0]*100) / salario)}%)                     : R$  {calculo[0]}
            (-) INSS ({int((calculo[1]*100) / salario)}%)                  : R$  {calculo[1]}
            FGTS (11%)                      : R$  {calculo[2]}
            Total de descontos              : R$  {calculo[3]}
            Salário Liquido                 : R$  {calculo[4]}
""")
