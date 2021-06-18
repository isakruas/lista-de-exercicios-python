"""
16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa
deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
        os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
from math import  sqrt
a = float(input('Qual o valor de a?\n'))
if a == 0:
    print('A equação não é do segundo grau\n')
    exit(0)
b = float(input('Qual o valor de b?\n'))
c = float(input('Qual o valor de c?\n'))
delta = b ** 2 - 4 * a * c
if delta < 0:
    print('A equação não possui raizes reais\n')
    exit(0)
if delta == 0:
    print('A equação possui apenas uma raiz real\n')
elif delta > 0:
    print('A equação possui duas raiz reais\n')
x_1 = (-1 * b - sqrt(delta)) / 2 * a
x_2 = (-1 * b + sqrt(delta)) / 2 * a

print(f'As raizes da equação são x_1 = {round(x_1, 2)} e x_2 = {round(x_2, 2)}\n')
