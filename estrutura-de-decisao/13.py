"""
13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
"""
dias = {
    '1': 'Domingo',
    '2': 'Segunda',
    '3': 'Tecça',
    '4': 'Quarta',
    '5': 'Quinta',
    '6': 'Sexta',
    '7': 'Sabado'
}
numero = input('Informe um número\n')
if numero in dias:
    print(f'{dias[numero]} é o dia correspondente da semana')
else:
    print('Valor inválido\n')
