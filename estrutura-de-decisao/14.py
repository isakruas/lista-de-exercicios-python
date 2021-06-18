"""
14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito
for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""
from statistics import mean
notas = set()
while True:
    try:
        nota = float(input(f'Informe a {len(notas)+1}º nota\n'))
        notas.add(nota)
        if len(notas) == 2:
            break
        pass
    except ValueError:
        pass
media = mean(notas)
conceito = ''
if 9.0 < media <= 10:
    conceito = 'A'
elif 7.5 < media <= 9.0:
    conceito = 'B'
elif 6.0 < media <= 7.5:
    conceito = 'C'
elif 4.0 < media <= 6.0:
    conceito = 'D'
elif 0 < media <= 4.0:
    conceito = 'E'

print(f'1º nota: {list(notas)[0]}\n2º nota: {list(notas)[1]}\nMédia de aproveitamento: {media}\nConceito: {conceito}\n')
if conceito in 'ABC':
    print('    APROVADO')
else:
    print('    REPROVADO')
