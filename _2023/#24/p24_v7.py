# Текстовый файл 24-222.txt содержит строку из символов A, B, C, D, E и F, всего не более чем 10^6 символов.
# Найдите максимальную длину строки вида А*А*А*А, где между буквами А расположены одинаковые группы символов,
# не содержащие букв А. Например, в строке BDADBADBADBABDAFABDA такая подстрока ADBADBADBA (длина 10).
#
# Ответ: 13

with open('24-222.txt') as f:
    strs = f.readline().strip().split('A')
    n = len(strs)
    mx = 0
    curLen = 0

    for i in range(n - 3):
        sr = strs[i:i + 3]

        if sr[0] == sr[1] == sr[2]:
            mx = max(mx, len(sr[0]) * 3 + 4)

    print(mx)
