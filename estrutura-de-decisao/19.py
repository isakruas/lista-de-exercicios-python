"""
19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades
do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10,
    21, 11, 1, 7 e 16
"""
while True:
    print('-' * 25)
    numero = input('Informe um número inteiro menor que 1000\n')
    if int(numero) >= 1000:
        print('O número invalido')
        pass
    if len(numero) == 1:
        print(f'{numero} = {numero[0]} unidade(s)')
    if len(numero) == 2:
        print(f'{numero} = {numero[-2]} dezena(s) e {numero[-1]} unidade(s)')
    if len(numero) == 3:
        print(f'{numero} = {numero[-3]} centena(s), {numero[-2]} dezena(s) e {numero[-1]} unidade(s)')
    pass
