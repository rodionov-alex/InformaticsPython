x = 32 ** 30 + 8 ** 60 - 32
c = 0

while x:
    if x % 4 == 3:
        c += 1
    x //= 4

print(c)
