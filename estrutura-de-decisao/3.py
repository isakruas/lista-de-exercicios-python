"""
3. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

while True:
    print('-' * 25)
    sexo = input('Escreva:\nF - Feminino\nM - Masculino\n')
    sexo = sexo.upper()
    if len(sexo) >= 2 or len(sexo) == 0:
        print('Sexo Inválido')
        pass
    if sexo[0] == 'M':
        print('Sexo Masculino')
        break
    elif sexo[0] == 'F':
        print('Sexo Feminino')
        break
    print('Sexo Inválido')
    pass
