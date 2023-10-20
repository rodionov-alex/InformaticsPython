from string import ascii_uppercase

for x in range(18, -1, -1):
    sx = str(x) if x < 10 else ascii_uppercase[x - 10]

    n1 = int('98897' + sx + '21', 19)
    n2 = int('2' + sx + '923', 19)
    val = n1 + n2

    if val % 18 == 0:
        print(val // 18)
        break

# Отвте: 469034148
