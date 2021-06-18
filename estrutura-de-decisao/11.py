"""
11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram
para desenvolver o programa que calculará os reajustes.
    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
    baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
"""
aumento = 0
salario = abs(float(input('Informe o salário\n')))
if 0 <= salario < 280:
    aumento = 0.20
elif 280 <= salario < 700:
    aumento = 0.15
elif 700 <= salario < 1500:
    aumento = 0.10
elif salario >= 1500:
    aumento = 0.05
print(f"""
Salário antes do reajuste: R$ {salario} 
Percentual de aumento aplicado: {aumento*100}%
Valor do aumento: R$ {aumento*salario}
Novo salário, após o aumento: R$ {(1+aumento)*salario}
""")
