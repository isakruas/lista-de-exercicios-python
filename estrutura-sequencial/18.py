"""
18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em
Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

tamanho_do_arquivo = float(input('Qual o tamanho do arquivo para download (em MB)?\n'))
velocidade_de_internet = float(input('Qual sua velocidade de Internet (em Mbps)?\n'))
tempo_em_segundos = tamanho_do_arquivo / (velocidade_de_internet / 10)
tempo_em_minutos = round(tempo_em_segundos / 60, 2)
print(f'O tempo aproximado de download do arquivo usando este link (em minutos) é de {tempo_em_minutos}\n')
