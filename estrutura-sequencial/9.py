"""
9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""
fahrenheit = float(input('Informe a temperatura em graus Fahrenheit\n'))
celsius = round(5 * ((fahrenheit-32) / 9), 2)
print(f'{fahrenheit} graus Fahrenheit equivale a {celsius} graus Celsius\n')
