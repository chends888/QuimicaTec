# -*- coding: utf-8 -*-

import time
import numpy as np


elementDict = {
        'Li' : (1, -3.05),
        'K' : (1, -2.93),
        'Ba' : (2, -2.90),
        'Sr' : (2, -2.89),
        'Ca' : (2, -2.87),
        'Na' : (1, -2.71),
        'Mg' : (2, -2.37),
        'Be' : (2, -1.85),
        'Al' : (3, -1.66),
        'Mn' : (2, -1.18),
        # '2h2o' : (2, -0.83),
        'Zn' : (2, -0.76),
        'Cr' : (3, -0.74),
        'Fe2' : (2, -0.44),
        'Cd' : (2, -0.40),
        'Pb(SO4)' : (2, -0.31),
        'Co' : (2, -0.28),
        'Ni' : (2, -0.25),
        'Sn2' : (2, -0.14),
        'Pb' : (2, -0.13),
        # '2h' : (2, 0.00),
        # 'sn4' : (2, 0.13),
        # 'cu' : (1, 0.15),
        # 'so4' : (2, 0.20),
        'AgCl' : (1, 0.22),
        'Cu2' : (2, 0.34),
        # 'o2+2h2o' : (4, 0.40),
        'I2' : (2, 0.53),
        'MnO4+2H2O' : (3, 0.59),
        # 'o2+2h' : (2, 0.68),
        'Fe3' : (1, 0.77),
        'Ag' : (1, 0.80),
        # 'hg' : (2, 0.85),
        # '2hg' : (2, 0.92),
        # 'no3' : (3, 0.96),
        # 'br2' : (2, 1.07),
        # 'o2+4h' : (4, 1.23),
        'MnO2' : (2, 1.23),
        # 'cr2o7' : (6, 1.33),
        # 'cl2' : (2, 1.36),
        'Au' : (3, 1.50),
        # 'mno4+8h' : (5, 1.51),
        # 'ce' : (1, 1.61),
        # 'h2o2' : (2, 1.77),
        # 'co' : (1, 1.82),
        # 'o3' : (2, 2.07),
        # 'f2' : (2, 2.87),
    
}

# while True:

print('''\nVocê deseja selecionar pilhas?[s]
Ou ver quais pilhas satisfazem uma tensão?[n]''')
func = input()
if func == 's':
    for key in elementDict:
        print(key)
    print('\nDigite o símbolo (um dos listados acima) do primeiro metal: ')
    element1Name = input()

    print('Digite o símbolo (um dos listados acima) do segundo metal: ')
    element2Name = input()

    print('\nPotencial de redução do', element1Name, ':',
        elementDict[element1Name][1], 'V')
    print('Potencial de redução do', element2Name, ':',
        elementDict[element2Name][1], 'V\n')

    if elementDict[element1Name][1] < elementDict[element2Name][1]:
        redPot = ((elementDict[element1Name][1]) -
            (elementDict[element2Name][1]))
        print ('O potencial da pilha teórico é de:', ('%.2f' % abs(redPot)), 'V')
        print('Portanto o', element2Name, 'reduz, e o', element1Name, 'oxida')
    else:
        redPot = ((elementDict[element2Name][1]) -
            (elementDict[element1Name][1]))
        print ('O potencial da pilha teórico é de:',
        ('%.2f' % abs(redPot)), 'V')
        print('Portanto o', element1Name, 'reduz, e o',
            element2Name, 'oxida')
    
    print('___________________________________________________________________')
    print('''\nEste resultdo considerou as soluções dos dois
eletrodos tendo a mesma concentração. Você deseja alterá-las?
Sim[s] ou Não[n]''')
    concent = input()

    if concent == 's' and elementDict[element1Name][0] == elementDict[element2Name][0]:
        #Cálculo do coeficiente da reação
        print('\nDigite a concentracao da solução (mol/L) do', element1Name, '(Ex: 2.1)')
        conc1 = float(input())
        print('Digite a concentracao da solução (mol/L) do', element2Name, '(Ex: 2.1)')
        conc2 = float(input())

        if elementDict[element1Name][1] < elementDict[element2Name][1]:
            coef = conc1/conc2
        else:
            coef = conc2/conc1
        
        #Equação de Nernst
        print('Qual a temperatura de operação das pilhas (em K)?')
        temp = float(input())

        nernst = abs(redPot) - ((8.315*temp)/(elementDict[element1Name][0]*96485)* np.log(coef))
        print('O novo potencial da  sua pilha é de:', ('%.2f' % abs(nernst)), 'V')

    else:
        print('Não foi possível calcular devido ao número diferente de elétrons')


else:
    print('\nDigite a tensão da sua aplicação (Ex: 1.2):')
    voltage = float(input())
    voltages = []
    if (voltage < 4.55 * 1.1):
        print('''\n\nVocê poderá usar as seguintes pilhas com uma tolerência de 10%
(sem nenhuma associação):''')
        for key in elementDict:
            for key2 in elementDict:
                if elementDict[key][1] == elementDict[key2][1]:
                    redPot = 0
                elif elementDict[key][1] < elementDict[key2][1]:
                    redPot = ((elementDict[key][1]) -
                    (elementDict[key2][1]))
                else:
                    redPot = ((elementDict[key2][1]) -
                    (elementDict[key][1]))
                if (voltage*0.9 < abs(redPot) and abs(redPot) <
                   voltage*1.1 and redPot not in voltages):
                    print(('%.2f' % abs(redPot)), 'V: ', key,'+',key2)
                    time.sleep(0.35)
                voltages.append(redPot)
    else:
        coef = 2
        while True: #(voltage*0.9 > abs(redPot) and abs(redPot) > voltage*1.1 and redPot not in voltages)
            for key in elementDict:
                for key2 in elementDict:
                    if elementDict[key][1] == elementDict[key2][1]:
                        redPot = 0
                    elif elementDict[key][1] < elementDict[key2][1]:
                        redPot = ((elementDict[key][1]) -
                        (elementDict[key2][1]))
                        redPot *= coef
                    else:
                        redPot = ((elementDict[key2][1]) -
                        (elementDict[key][1]))
                        redPot *= coef
                    if (voltage*0.9 < abs(redPot) and abs(redPot) <
                       voltage*1.1 and redPot not in voltages):
                        print(('%.2f' % abs(redPot)), 'V com', coef, 'pilhas:', key,'+',key2)
                        time.sleep(0.35)
                        voltages.append(redPot)
            coef += 1
            # print(voltages)
            # print('Loop')
            if (not voltages):
               continue
            else:
                # print('end')
                break



# Referências Bibliográficas:

    # Tabela de potenciais padrão: 
    # http://www.dqi.iq.ufrj.br/tabela_de_potenciais.pdf