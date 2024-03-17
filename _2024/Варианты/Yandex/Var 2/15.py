data = {-42, -10, -8, 2, 16, -10, -4, 2, 15, 23}
res = []
longest = 1
value = 1

for x in range(-42, 24):
    B = x in {-42, -10, -8, 2, 16}
    C = x in {-10, -4, 2, 15, 23}
    A = longest

    f = (A <= B) or C

    if f != ((not longest) == value) and x > 0:
        res.append(x)

print(sum(res))

