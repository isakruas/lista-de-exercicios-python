"""
18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""
from datetime import datetime, timedelta
data = input('Informe uma data no formato dd/mm/aaaa\n')
data = data.split('/')
if len(data) != 3:
    data = '/'.join(str(el) for el in data)
    print(f'{data} é uma data inválida\n')
    exit(0)
if (1 <= int(data[0]) <= 31) and (1 <= int(data[1]) <= 12):
    if int(data[1]) == 2:
        if (datetime(int(data[2]), 2, 28) + timedelta(days=1)).month == 2:
            if int(data[0]) <= 29:
                data = '/'.join(str(el) for el in data)
                print(f'{data} é uma data válida\n')
                exit(0)
            else:
                data = '/'.join(str(el) for el in data)
                print(f'{data} é uma data inválida\n')
                exit(0)
        else:
            if int(data[0]) <= 28:
                data = '/'.join(str(el) for el in data)
                print(f'{data} é uma data válida\n')
                exit(0)
            else:
                data = '/'.join(str(el) for el in data)
                print(f'{data} é uma data inválida\n')
                exit(0)
    else:
        data = '/'.join(str(el) for el in data)
        print(f'{data} é uma data válida\n')
        exit(0)
else:
    data = '/'.join(str(el) for el in data)
    print(f'{data} é uma data inválida\n')
    exit(0)
