# -*- coding: utf-8 -*-

# Referências Bibliográficas:

    # Tabela de potenciais padrão: 
    # http://www.dqi.iq.ufrj.br/tabela_de_potenciais.pdf

import time
import numpy as np

elementDict = {
    #Metal : (número de elétrons, potencial de redução)
    'Li'        : (1, -3.05, 6,94),
    'K'         : (1, -2.93, 39.09),
    'Ba'        : (2, -2.90, 137,33),
    'Sr'        : (2, -2.89, 87.62),
    'Ca'        : (2, -2.87, 40.08),
    'Na'        : (1, -2.71, 22.99),
    'Mg'        : (2, -2.37, 24.30),
    'Be'        : (2, -1.85, 9.01),
    'Al'        : (3, -1.66, 26.98),
    'Mn'        : (2, -1.18, 54.93),
    'Zn'        : (2, -0.76, 65.38),
    'Cr'        : (3, -0.74, 51.96),
    'Fe2'       : (2, -0.44, 55.84),
    'Cd'        : (2, -0.40, 112.41),
    'Pb(SO4)'   : (2, -0.31, 303.26),
    'Co'        : (2, -0.28, 58.93),
    'Ni'        : (2, -0.25, 58.69),
    'Sn2'       : (2, -0.14, 118.71),
    'Pb'        : (2, -0.13, 207.2),
    'AgCl'      : (1, 0.22, 143.32),
    'Cu2'       : (2, 0.34, 63.54),
    'I2'        : (2, 0.53, 393.8),
    'MnO4+2H2O' : (3, 0.59, 154,97),
    'Fe3'       : (1, 0.77, 55.84),
    'Ag'        : (1, 0.80, 107.87),
    'MnO2'      : (2, 1.23, 86.93),
    'Au'        : (3, 1.50, 196.97),
    # '2h2o' : (2, -0.83),
    # '2h' : (2, 0.00),
    # 'sn4' : (2, 0.13),
    # 'cu' : (1, 0.15),
    # 'so4' : (2, 0.20),
    # 'o2+2h2o' : (4, 0.40),
    # 'o2+2h' : (2, 0.68),
    # 'hg' : (2, 0.85),
    # '2hg' : (2, 0.92),
    # 'no3' : (3, 0.96),
    # 'br2' : (2, 1.07),
    # 'o2+4h' : (4, 1.23),
    # 'cr2o7' : (6, 1.33),
    # 'cl2' : (2, 1.36),
    # 'mno4+8h' : (5, 1.51),
    # 'ce' : (1, 1.61),
    # 'h2o2' : (2, 1.77),
    # 'co' : (1, 1.82),
    # 'o3' : (2, 2.07),
    # 'f2' : (2, 2.87),
}
solutionDict = {
    #Metal : (número de elétrons, potencial de redução)
    'MnO4'   : (1, []),
    'NO2'    : (1, []),
    'NO3'    : (1, []),
    'ClO3'   : (1, []),
    'ClO4'   : (1, ['K']),
    'C2H3O2' : (1, ['Ag']),
    'SCN'    : (1, ['Ag', 'Pb']),
    'S2O3'   : (2, ['Ag', 'Pb']),
    'F'      : (1, ['Mn', 'Ca', 'Sr']),
    'Cl'     : (1, ['Ag', 'Pb']),
    'Br'     : (1, ['Ag', 'Pb']),
    'I'      : (1, []),
    'SO4'    : (2, ['Ag', 'Pb', 'Ba', 'Sr']),
}

def calcElet(element1Name, element2Name):
    #Calculando número de elétrons da reação global para usos futuros
    nElet = elementDict[element2Name][0]*elementDict[element1Name][0]
    if nElet == 6:
        return 3
    if nElet == 4:
        return 2
    else:
        return 1

def calcVolt(element1Name, element2Name):
    if elementDict[element1Name][1] < elementDict[element2Name][1]:
        return ((elementDict[element1Name][1]) - (elementDict[element2Name][1]))
    else:
        return ((elementDict[element2Name][1]) - (elementDict[element1Name][1]))

def calcCap(elem1Mol, elem2Mol, nElet):
    bat1Cap = (elem1Mol * nElet * 96485)/(3600)
    bat2Cap = (elem2Mol * nElet * 96485)/(3600)
    return (bat1Cap, bat2Cap)

print('''\nVocê deseja montar uma pilha?[s]
Ou inserir dados e obter as opções de pilhas?[n]''')
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

    redPot = calcVolt(element1Name, element2Name)
    print ('O potencial da pilha teórico é de:', ('%.2f' % abs(redPot)), 'V')
    print('Portanto o', element2Name, 'reduz, e o', element1Name, 'oxida')

    print('\n___________________________________________________________________')
    print('''Este resultado considerou as soluções dos dois
eletrodos tendo a mesma concentração. Você deseja alterá-las?
Sim[s] ou Não[n]''')
    concent = input()

    if concent == 's':
        #Cálculo do coeficiente da reação
        print('\nDigite a concentracao da solução (mol/L) do', element1Name, '(Ex: 2.1)')
        conc1 = float(input())
        print('Digite a concentracao da solução (mol/L) do', element2Name, '(Ex: 2.1)')
        conc2 = float(input())

        coef = (conc1**elementDict[element2Name][0]) / (conc2**elementDict[element1Name][0])

        #Equação de Nernst
        print('Qual a temperatura de operação das pilhas (em K)?')
        temp = float(input())

        print('Constante de equilíbrio:', str(coef).replace('.',','))

        nElet = calcElet(element1Name, element2Name)
        nernst = abs(redPot) - ((8.315*temp)/(nElet*96485)* np.log(coef))
        print('O novo potencial da  sua pilha é de:', str(('%.3f' % abs(nernst))).replace('.',','), 'V')

    print('\n___________________________________________________________________')
    print('Você deseja alterar as soluções dos metais? Sim[s] ou Não[n]')
    sol = input()

    if sol == 's':
        print('\nSelecione a solução do', element1Name,'entre as opções abaixo:')
        for key in solutionDict:
            if element1Name not in solutionDict[key][1]:
                print(key)
        sol1 = input()

        print('\nSelecione a solução do', element2Name,'entre as opções abaixo:')
        for key in solutionDict:
            if element2Name not in solutionDict[key][1]:
                print(key)
        sol2 = input()

        print('\n\nFórmula da solução do', element1Name,':', element1Name+str(solutionDict[sol1][0])+'('+sol1+')'+str(elementDict[element1Name][0]))
        print('Fórmula da solução do', element2Name,':', element2Name+str(solutionDict[sol2][0])+'('+sol2+')'+str(elementDict[element2Name][0]))

    print('\n___________________________________________________________________')
    print('Deseja calcular a capacidade de carga? Sim[s] ou Não[n]?')
    capacity = input()
    if capacity == 's':
        print('Insira a massa de', element1Name, ' (em gramas, ex: 345):')
        elem1Mass = float(input())
        print('Insira a massa de', element2Name, '(em gramas, ex: 1.23):')
        elem2Mass = float(input())

        elem1Mol = elem1Mass/elementDict[element1Name][2]
        elem2Mol = elem2Mass/elementDict[element2Name][2]

        nElet = calcElet(element1Name, element2Name)
        batCap = calcCap(elem1Mol, elem2Mol, nElet)

        if batCap[0] < batCap[1]:
            print('\nCapacidade de carga é:', str(('%.3f' % abs(batCap[0]))).replace('.',','), 'Ah. E o elemento limitante é o', element1Name)
        else:
            print('Capacidade de carga é:', str(('%.3f' % abs(batCap[1]))).replace('.',','), 'Ah. E o elemento limitante é o', element2Name)



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
                    print(str(('%.2f' % abs(redPot))).replace('.',','), 'V: ', key,'+',key2)
                    time.sleep(0.15)
                voltages.append(redPot)
    else:
        print('\n\nVocê poderá usar as seguintes pilhas (tolerência de 10%):')
        coef = 2
        assocDict = {}
        counter = 1
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
                        print(counter, '-', str(('%.2f' % abs(redPot))).replace('.',','), 'V com', coef, 'pilhas em série:', key,'+',key2)
                        time.sleep(0.15)
                        assocDict[counter] = (abs(redPot), key, key2)
                        voltages.append(redPot)
                        counter += 1
            coef += 1
            # print(voltages)
            # print('Loop')
            if (not voltages):
               continue
            else:
                break
    print('\nEscolha uma das opções acima:')
    batOption = int(input())
    print('\nDigite a potência de sua aplicação (em watts) (Ex: 3.1):')
    pot = float(input())
    print('\nDigite o seu tempo de uso (em horas) (Ex: 5):')
    lifespan = float(input())

    voltage = calcVolt(assocDict[batOption][1], assocDict[batOption][2])
    # print(assocDict[batOption][0])
    curr = float(pot)/assocDict[batOption][0]
    nElet = calcElet(assocDict[batOption][1], assocDict[batOption][2])
    cap = calcCap(1, 1, nElet)
    load = curr * lifespan

    print('\nCorrente máxima da sua aplicação é:', str('%.3f' % curr).replace('.',','), 'A')

    counter = 2
    capa = cap[0]
    if (load > capa):
        while True:
            capa += cap[0]
            if load < capa:
                break
            counter += 1

    print('E a carga necessária:', str('%.3f' % load).replace('.',','), 'Ah')

    if counter == 2:
        print('A capacidade de carga:', str('%.3f' % abs(cap[0])).replace('.',','), 'Ah')
    else:
        print('Será necessário associar', str(counter), 'do conjunto', str(batOption)+',', 'sendo a capacidade de carga resultante:', str('%.3f' % abs((cap[0])*counter)).replace('.',','), 'Ah')





    # print('\nDigite a capacidade da sua aplicação (em Ah, ex: 23.8):')
    # cap = float(input())

    # print('\nCom uma tolarência de 10%, você tem as seguintes opções:')
    # coef = 1
    # while True:
    #     capacities = []
    #     for key in elementDict:
    #         for key2 in elementDict:
    #             batCap = ((calcElet(key, key2) * 96485) / 3600) * coef
    #             print(key, key2)
    #             print(batCap)
    #             print(coef)
    #             time.sleep(0.05)
    #             if (cap*0.9 < abs(batCap) and abs(batCap) < cap*1.1):
    #                 print(('%.2f' % abs(batCap), 'Ah, utilizando pilhas de:', key, '+', key2))
    #                 time.sleep(0.35)
    #     coef += 1
    #     if (not capacities):
    #         continue
    #     else:
    #         break