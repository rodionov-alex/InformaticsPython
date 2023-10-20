from tqdm import tqdm

pifs = 0
max_pif = 0
max_c = 0

for a in tqdm(range(1, 5001)):
    for b in range(a, 5001):
        r_c = (a * a + b * b) ** 0.5
        c = int(r_c)

        if c == r_c and c <= 5000=][]
            pifs += 1
            pif = a + b + c

            if max_pif < pif:
                max_pif = pif
                max_c = c

print(pifs, max_c)
# 5681 4988
