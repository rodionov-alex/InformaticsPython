from itertools import product

print(*[bin(x)[2:].zfill(8) for x in (212, 192, 32, 96)])
print(*[bin(x)[2:].zfill(8) for x in (255, 255, 255, 224)])
count = 0

for p in product('01', repeat=5):
    byte = '011' + ''.join(p)
    if '111' not in byte and '000' not in byte:
        count += 1

print(count)
