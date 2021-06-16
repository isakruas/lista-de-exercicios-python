"""
15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""

ganho_por_hora = float(input('Quanto você ganha por hora?\n'))
horas_trabalhadas = float(input('Qual o número de horas trabalhadas no mês?\n'))
salario_bruto = ganho_por_hora * horas_trabalhadas
imposto_de_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (imposto_de_renda + inss + sindicato)
print(f"""
+ Salário Bruto : R$ {salario_bruto}
- IR (11%) : R$ {imposto_de_renda}
- INSS (8%) : R$ {inss}
- Sindicato ( 5%) : R$ {sindicato}
= Salário Liquido : R$ {salario_liquido}
""")
