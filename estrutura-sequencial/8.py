"""
8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês.
"""
ganho_por_hora = float(input('Informe quanto você ganha por hora\n'))
horas_trabalhadas_no_mes = float(input('Informe a quantidade de horas trabalhadas no mês\n'))
total_do_salario = ganho_por_hora*horas_trabalhadas_no_mes
print(f'O total do seu salário no referido mês é {total_do_salario}\n')
