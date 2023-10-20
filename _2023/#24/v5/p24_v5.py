# Текстовый файл 24-224.txt содержит строку из символов A, B и C, всего не более чем 10^6 символов. Найдите
# максимальную длину строки, состоящей только из комбинаций BAC и СAB. Например, в строке BABABACCABCABCB
# такая подстрока BACCABCAB (длина 9).
#
# Ответ: 72

with open('24-224.txt') as f:
    s = f.readline().strip()

    # Возможны 2 варианта в зависимости от того, с какой комбинации начинать считать:
    # 1. BACABCAB - если с BAC то длина будет 3, а если с CAB то длина будет уже 6
    # 2. CABACBAC - если с CAB то длина будет 3, а если с BAC то длина будет уже 6

    # 1) сначала считаем количество BAC, а потом CAB
    s1 = s.replace('BAC', '*').replace('CAB', '*')
    # 2) сначала считаем количество CAB, а потом BAC
    s2 = s.replace('CAB', '*').replace('BAC', '*')
    n1 = len(s1)
    n2 = len(s2)
    mx = 0
    curLen = 0

    # Проверка 1 варианта
    for ch in s1:
        if ch == '*':
            curLen += 3
        else:
            mx = max(mx, curLen)
            curLen = 0

    mx = max(mx, curLen)
    curLen = 0

    # Проверка 2 варианта
    for ch in s2:
        if ch == '*':
            curLen += 3
        else:
            mx = max(mx, curLen)
            curLen = 0

    mx = max(mx, curLen)

    print(mx)
