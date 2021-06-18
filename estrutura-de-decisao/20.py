"""
20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada
por aluno e presentar:

    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10.

OBS:
    Semelhante a questão 5
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
    elif mean(notas) == 10:
        print(f'Aprovado com Distinção, media {round(mean(notas), 2)}')
    elif mean(notas) < 7:
        print(f'Reprovado, media {round(mean(notas), 2)}')
