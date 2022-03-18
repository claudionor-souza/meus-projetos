from math import ceil
import time

time.sleep(0)
print('='*40)
print('{:^40}'.format('CALCULADORA PARA REVESTIMENTO - MOD. 0 - CÁLCULO SIMPLES'))
print('='*40)
print('DIMENSÕES DA ÁREA:')
altura_parede = float(input('Altura da parede: '))
largura_parede = float(input('Largura da parede: '))
time.sleep(1)
print('='*40)
print('DIMENSÕES DO REVESTIMENTO:')
largura_revestimento = float(input('Largura do revestimento: '))
altura_revestimento = float(input('Altura do revestimento: '))
revestimento = largura_revestimento * altura_revestimento
area_total = largura_parede * altura_parede
qtd = (area_total / revestimento) + (area_total / revestimento) * 10/100
time.sleep(1)
print('='*40)
print('CALCULANDO...')
print('='*40)
time.sleep(3)
print('RESULTADO:')
print(f'Área total: {area_total:.2f}M²')
print(f'Quantidade de revestimentos: {ceil(qtd)} unidades')
time.sleep(5)
print('='*40)
print('PROGRAMA ENCERRADO')
print('='*40)