f = open(r'F:\Informatics\Python\Igor Lazu\#24\v3\test_24.txt')

maxAB = 0
resNoC = ''
resNoBB = ''
resStr = ''

for line in f:
    noC_strings = line.split('C') #список строк без 'C'

    for noC_str in noC_strings:
        noBB_strings = [] #список строк без 'BB'
        
        #если в строке есть сочетания 'BB' то разобьем ее на подстроки
        if noC_str.count('BB') > 0:
            noBB_strings = noC_str.split('BB')
            noBB_count = len(noBB_strings)
            
            #так как метод split() "уничтожит" сочетания 'BB', то мы должны восстановить 'B' в конце каждой подстроки кроме последней
            for i in range(noBB_count - 1):
                noBB_strings[i] += 'B'
        #если в строке нет сочетания 'BB' то просто копируем строку
        else:
            noBB_strings.append(noC_str)

        for noBB_str in noBB_strings:
            noAA_strings = [] #список строк без 'AA'

            #если в строке есть сочетания 'AA' то разобьем ее на подстроки
            if noBB_str.count('AA') > 0:
                noAA_strings = noBB_str.split('AA')
                noAA_count = len(noAA_strings)

                #так как метод split() "уничтожит" сочетания 'AA', то мы должны восстановить 'A'
                for i in range(noAA_count):
                    #если 'AA' в начале строки noBB_str, то добавляем в конце первой подстроки 'A'
                    if i == 0:
                        noAA_strings[i] += 'A'
                    #если 'AA' в конце строки noBB_str, то добавляем в начале последней подстроки 'A'
                    elif i == noAA_count - 1:
                        noAA_strings[i] = 'A' + noAA_strings[i]
                    #в остальных подстроках 'A' добавляется и в начале и в конце
                    else:
                        noAA_strings[i] = 'A' + noAA_strings[i] + 'A'
            #если в строке нет сочетания 'AA' то просто копируем строку
            else:
                noAA_strings.append(noBB_str)

            for noAA_str in noAA_strings:
                lAB = len(noAA_str)

                if maxAB < lAB:
                    maxAB = lAB
                    resNoC = noC_str
                    resNoBB = noBB_str
                    resStr = noAA_str

print('Ответ:', maxAB)
print('  No C str:', resNoC)
print(' No BB str:', resNoBB)
print('Result str:', resStr)