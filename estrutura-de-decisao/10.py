"""
10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-
Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
while True:
    print('-' * 26)
    turno = input('Em que turno você estuda?\n[M] - Matutino\n[V] - Vespertino\n[N] - Noturno\n')
    if len(turno) == 0:
        print('Valor Inválido!')
        pass
    turno = turno[0].upper()
    if turno == 'M':
        print('Bom Dia!')
        print('-' * 26)
        break
    elif turno == 'V':
        print('Boa Tarde!')
        print('-' * 26)
        break
    elif turno == 'N':
        print('Boa Noite!')
        print('-' * 26)
        break
    else:
        print('Valor Inválido!')
        pass
