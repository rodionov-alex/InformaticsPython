from tqdm import tqdm

f = open('b.txt')
lines = f.readlines()[1:]
pr = [int(i) for i in lines]
f.close()
l = len(pr)
k = 0

for i in tqdm(range(l-2)):
    s = 0
    for j in range(i + 2, l):
        s += pr[j-1]
        if (pr[i] + pr[j]) % 3 == 0 and s == 0:
            k += 1

print(k)