"""
10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""
celsius = float(input('Informe a temperatura em graus Celsius\n'))
fahrenheit = round(9 * (celsius / 5) + 32, 2)
print(f'{celsius} graus Celsius equivale a {fahrenheit} graus Fahrenheit\n')
