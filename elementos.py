elementDict = {
    'li' : (1, -3.05),
    'k' : (1, -2.93),
    'ba' : (2, -2.90),
    'sr' : (2, -2.89),
    'ca' : (2, -2.87),
    'na' : (1, -2.71),
    'mg' : (2, -2.37),
    'be' : (2, -1.85),
    'al' : (3, -1.66),
    'mn' : (2, -1.18),
    '2h2o' : (2, -0.83),
    'zn' : (2, -0.76),
    'cr' : (3, -0.74),
    'fe2' : (2, -0.44),
    'cd' : (2, -0.40),
    'pbso4' : (2, -0.31),
    'co' : (2, -0.28),
    'ni' : (2, -0.25),
    'sn2' : (2, -0.14),
    'pb' : (2, -0.13),
    '2h' : (2, 0.00),
    'sn4' : (2, 0.13),
    'cu' : (1, 0.15),
    'so4' : (2, 0.20),
    'agcl' : (1, 0.22),
    'cu2' : (2, 0.34),
    'o2+2h2o' : (4, 0.40),
    'i2' : (2, 0.53),
    'mno4+2h2o' : (3, 0.59),
    'o2+2h' : (2, 0.68),
    'fe3' : (1, 0.77),
    'ag' : (1, 0.80),
    'hg' : (2, 0.85),
    '2hg' : (2, 0.92),
    'no3' : (3, 0.96),
    'br2' : (2, 1.07),
    'o2+4h' : (4, 1.23),
    'mno2' : (2, 1.23),
    'cr2o7' : (6, 1.33),
    'cl2' : (2, 1.36),
    'au' : (3, 1.50),
    'mno4+8h' : (5, 1.51),
    'ce' : (1, 1.61),
    'h2o2' : (2, 1.77),
    'co' : (1, 1.82),
    'o3' : (2, 2.07),
    'f2' : (2, 2.87),
    
}

class Element:
    elementDict = {
        'li' : (1, -3.05),
        'k' : (1, -2.93),
        'ba' : (2, -2.90),
        'sr' : (2, -2.89),
        'ca' : (2, -2.87),
        'na' : (1, -2.71),
        'mg' : (2, -2.37),
        'be' : (2, -1.85),
        'al' : (3, -1.66),
        'mn' : (2, -1.18),
        '2h2o' : (2, -0.83),
        'zn' : (2, -0.76),
        'cr' : (3, -0.74),
        'fe2' : (2, -0.44),
        'cd' : (2, -0.40),
        'pbso4' : (2, -0.31),
        'co' : (2, -0.28),
        'ni' : (2, -0.25),
        'sn2' : (2, -0.14),
        'pb' : (2, -0.13),
        '2h' : (2, 0.00),
        'sn4' : (2, 0.13),
        'cu' : (1, 0.15),
        'so4' : (2, 0.20),
        'agcl' : (1, 0.22),
        'cu2' : (2, 0.34),
        'o2+2h2o' : (4, 0.40),
        'i2' : (2, 0.53),
        'mno4+2h2o' : (3, 0.59),
        'o2+2h' : (2, 0.68),
        'fe3' : (1, 0.77),
        'ag' : (1, 0.80),
        'hg' : (2, 0.85),
        '2hg' : (2, 0.92),
        'no3' : (3, 0.96),
        'br2' : (2, 1.07),
        'o2+4h' : (4, 1.23),
        'mno2' : (2, 1.23),
        'cr2o7' : (6, 1.33),
        'cl2' : (2, 1.36),
        'au' : (3, 1.50),
        'mno4+8h' : (5, 1.51),
        'ce' : (1, 1.61),
        'h2o2' : (2, 1.77),
        'co' : (1, 1.82),
        'o3' : (2, 2.07),
        'f2' : (2, 2.87),
        
    }

# while True:
element = Element()
for key in elementDict:
    print(key)
# print(elementDict)
print('Digite o símbolo (um dos listados acima) do primeiro elemento: ')
element1Name = input()

print('Digite o símbolo (um dos listados acima) do segundo elemento: ')
element2Name = input()
print("\n")

print('Potencial de redução do', element1Name, ':', element.elementDict[element1Name][1], 'V')
print('Potencial de redução do', element2Name, ':', element.elementDict[element2Name][1], 'V\n')

if element.elementDict[element1Name][1] < element.elementDict[element2Name][1]:
    redPot = (element.elementDict[element1Name][1]) - (element.elementDict[element2Name][1])
    print ('O potencial da pilha teórico é de:', ('%.2f' % abs(redPot)), 'V')
    print('Portanto o', element2Name, 'reduz, e o', element1Name, 'oxida')
else:
    redPot = (element.elementDict[element2Name][1]) - (element.elementDict[element1Name][1])
    print ('O potencial da pilha teórico é de:', ('%.2f' % abs(redPot)), 'V')
    print('Portanto o', element1Name, 'reduz, e o', element2Name, 'oxida')




# Referências Bibliográficas:

    # Tabela de potenciais padrão: 
    # http://www.dqi.iq.ufrj.br/tabela_de_potenciais.pdf