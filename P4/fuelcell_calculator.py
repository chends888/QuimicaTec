import time
import math

'''
Parâmetros iniciais
'''
# Densidade de corrente 0,367 A/cm2
curr_density = 0.367
# Pressão do H2 e O2: Pressão atmosférica

# Temp.: 25ºC
c_temp = 25
k_temp = 298

# Área: 100 cm2
max_area = 100

# Corrente máxima: 367 A
max_curr = 367

# Tensão: 1,23 V
unit_voltage = 1.23

# ar = 21% oxigênio


print('\n----------- Bem-vindo à calculadora de células de combustível -----------\n')

time.sleep(0.7)
print('Insira a tensão de sua aplicação para iniciar, em Volts (Ex: 24.3):')
voltage = float(input())

time.sleep(0.7)
print('\nInsira a corrente máxima, em Amperes (Ex: 2.2). Ou pressione "Enter" para inserir a potência')
curr = input()

if(curr == ''):
    time.sleep(0.7)
    print('\nInsira a potêcia da aplicação, em Watts (Ex: 25.5):')
    pot = float(input())
    curr = float(pot/voltage)
else:
    curr = float(curr)

time.sleep(0.7)
print('\nInsira o tempo de uso desejado, em horas (Ex: 25.5):')
usage = float(input())


total_load = curr*usage
cell_num = math.ceil(voltage/unit_voltage)

# Calcular quantidade de mols, massa e vazão de H2
h2_mass = curr/96485
h2_mols = h2_mass/2
h2_flow = h2_mass/usage

# Calcular quantidade de mols, massa e vazão de ar atmosférico
o2_mols = h2_mols/2
o2_mass = o2_mols*32
air_flow = (o2_mass/0.21)/usage


time.sleep(0.7)
print('\n\nNúmero total de mols de H2 consumidos:', h2_mols, 'mols')
time.sleep(0.1)
print('Massa total de de H2 consumidos:', h2_mass, 'g')
time.sleep(0.1)
print('Número mínimo de células associadas em série:', cell_num, 'células')
time.sleep(0.1)
print('Vazão de H2:', h2_flow, 'g/h')
time.sleep(0.1)
print('Vazão de ar atmosférico:', air_flow, 'g/h')
time.sleep(0.1)
print('Capacidade de carga total:', round(total_load, 2), 'Ah')