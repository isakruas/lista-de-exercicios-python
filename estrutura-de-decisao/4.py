"""
4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
vogais = 'aeiou'
letra = input('Informe uma letra\n')
letra = letra[0].lower()
if letra in vogais:
    print(f'A letra {letra} informada é uma vogal')
else:
    try:
        int(letra)
        print('Você não informou uma letra')
    except ValueError:
        print(f'A letra {letra} informada é uma consoante')
