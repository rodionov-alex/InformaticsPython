x = abs(18 * 7 ** 108 - 5 * (49 ** 76) + 343 ** 35 - 50)
sm = 0

while x:
    sm += x % 49
    x //= 49

print(sm)