print(*[bin(x)[2:].zfill(8) for x in (192, 168, 76, 160)])
print(*[bin(x)[2:].zfill(8) for x in (255, 255, 255, 240)])
ct = 0

for n in range(1, 15):
    if n % 2 == 0 and bin(n).count('1') % 2 == 0:
        ct += 1

print(ct)
