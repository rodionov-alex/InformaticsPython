def count_divs(num):
    divs = set()

    for d in range(1, int(num ** 0.5) + 1):
        if num % d == 0:
            divs.add(d)
            divs.add(num // d)

    return len(divs)

md = 0
mn = 0

for n in range(394441, 394506):
    cd = count_divs(n)

    if cd > md:
        md = cd
        mn = n

print(md, mn)