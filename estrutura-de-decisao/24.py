"""
24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
"""
numeros = list()
resultado = None
while True:
    if len(numeros) < 2:
        numero = float(input(f'Informe o {len(numeros) + 1}º número\n'))
        numeros.append(numero)
    if len(numeros) == 2:
        operacao = input('Qual operação deseja realizar?\n[1] +\n[2] -\n[3] /\n[4] *\n')
        if operacao == '1':
            resultado = numeros[0] + numeros[1]
            break
        elif operacao == '2':
            resultado = numeros[0] - numeros[1]
            break
        elif operacao == '3':
            resultado = numeros[0] / numeros[1]
            break
        elif operacao == '4':
            resultado = numeros[0] * numeros[1]
            break
        else:
            pass

print(f'O resultado da operação foi {resultado}')
if resultado % 2 == 0:
    print(f'O resultado {resultado} é par')
elif resultado % 2 == 1:
    print(f'O resultado {resultado} é impar')
if resultado > 0:
    print(f'O resultado {resultado} é positivo')
else:
    print(f'O resultado {resultado} é negativo')
if (resultado * 10) % 10 != 0:
    print(f'O resultado {resultado} é decimal')
else:
    print(f'O resultado {resultado} é inteiro')
