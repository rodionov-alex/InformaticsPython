def f(n):
    bn = bin(n)[2:]
    if n % 2:
        bn = '1' + bn + '01'
    else:
        bn += '10'

    return int(bn, 2)


i = 0
j = 0

while j <= 516:
    i += 1
    j = f(i)

print(i)