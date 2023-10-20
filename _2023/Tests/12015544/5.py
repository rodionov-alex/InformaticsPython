for n in range(9999, 999, -1):
    digits = [int(x) for x in str(n)]
    r = [digits[0] + digits[1], digits[1] + digits[2], digits[2] + digits[3]]
    r.remove(min(r))
    r.sort()
    r = ''.join([str(x) for x in r])

    if r == '1517':
        print(n)
        break
