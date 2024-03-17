r = n = 0

while r <= 2000:
    n += 1
    br = bin(n)[2:]

    if n % 2 == 0:
        br = br + ('0' * br.count('0'))
    else:
        br = ('1' * br.count('1')) + br

    r = int(br, 2)

print(n)
