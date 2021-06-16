"""
13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
que calcule seu peso ideal, utilizando as seguintes fórmulas:
    a. Para homens: (72.7*h) - 58
    b. Para mulheres: (62.1*h) - 44.7
"""
homen = bool(int(input('Digite\n[0] Se for uma mulher\n[1] Se for um homem\n')))
altura = float(input('Informe sua altura\n'))
if homen:
    peso_ideal = round((72.7 * altura) - 58, 2)
else:
    peso_ideal = round((62.1 * altura) - 44.7, 2)
print(f'Seu peso ideal é {peso_ideal}\n')
