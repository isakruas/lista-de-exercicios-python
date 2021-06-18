"""
25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

    O programa deve no final emitir uma classificação sobre a participação da pessoa
     no crime.

     Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4
     como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
print('Sobre o crime, responda S para sim ou N para não\n')
perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?',
             'Já trabalhou com a vítima?']
i = 0
classificacao = 0
while True:
    if i + 1 > len(perguntas):
        break
    resposta = input(perguntas[i] + '\n')
    if len(resposta) == 0:
        pass
    resposta = resposta[0].upper()
    if resposta == 'S':
        classificacao += 1
    i += 1
    pass

if classificacao == 2:
    print('Você está classificado(a) como "Suspeito(a)"')
elif 3 <= classificacao <= 4:
    print('Você está classificado(a) como "Cúmplice"')
elif classificacao == 5:
    print('Você está classificado(a) como "Assassino"')
else:
    print('Você está classificado(a) como "Inocente"')
