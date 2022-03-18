from math import ceil
r = 'S'
print('<<>>' * 9)
print('{:^40}'.format('CALCULADORA DE BLOCOS'))
print('<<>>' * 9)
while r == 'S':
    print('''Escolha um tipo de bloco:
[1]Bloco 6 furos 09X14X19
[2]Bloco 8 furos 09X19X19
[3]Bloco 9 furos 11,5X14X24''')
    opção = int(input('\033[1;34mQual a sua opção:\033[m '))
    larg = float(input('\033[1;34mDigite a largura: \033[m'))
    alt = float(input('\033[1;34mDigite a altura: \033[m'))
    area = larg * alt
    if opção == 1:
        qtd = area / 0.0266
        print('\033[1;33mSerão necessários {} blocos\033[m'.format(ceil(qtd)))
    elif opção == 2:
        qtd = area / 0.0361
        print('\033[1;33mSerão necessários {} blocos de 09X19X19\033[m'.format(ceil(qtd)))
    elif opção == 3:
        qtd = area / 0.0336
        print('\033[1;33mSerão necessários {} blocos\033[m'.format(ceil(qtd)))
    r = str(input('\033[1;31mDeseja continuar? [S/N] \033[m')).upper()
print('\033[7;40mPrograma finalizado\033[m')
