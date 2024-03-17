ip = (20, 24, 110, 42)
ad = (20, 24, 96, 0)

print(*[bin(x)[2:].zfill(8) for x in ip])
print(*[bin(x)[2:].zfill(8) for x in ad])
