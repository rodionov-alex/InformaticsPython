points = [101, 143, 144, 199]
longest = 1
value = 1

for x in [i / 4 for i in range(min(points) * 4, max(points) * 4 + 1)]:
    B = 101 <= x <= 143
    C = 144 <= x <= 199
    A = longest
    f = A <= (B or C)

    if f != ((not longest) == value):
        print(x)

res = []

for x in range(1000):
    B = 101 <= x <= 143
    C = 144 <= x <= 199
    A = 144 <= x <= 199
    f = A <= (B or C)

    if f != value:
        res.append(x)

print(res)
print(199 - 144)
