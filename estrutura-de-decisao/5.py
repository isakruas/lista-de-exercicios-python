"""
5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular
a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
from statistics import mean
notas = []
while True:
    nota = input('Informe uma nota parcial ou irforme calcular para proceguir\n')
    if nota == 'calcular':
        break
    else:
        try:
            notas.append(float(nota))
        except ValueError:
            pass
if len(notas) == 0:
    print('Você não informou notas\n')
else:
    if 7 <= mean(notas) < 10:
        print(f'Aprovado, media {round(mean(notas), 2)}')
    elif mean(notas) >= 10:
        print(f'Aprovado com Distinção, media {round(mean(notas), 2)}')
    elif mean(notas) < 7:
        print(f'Reprovado, media {round(mean(notas), 2)}')
