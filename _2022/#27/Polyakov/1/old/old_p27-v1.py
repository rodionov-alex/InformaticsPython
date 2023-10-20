from tqdm import tqdm


def gcd(a, b):
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def is_good(numb):
    return ((numb % 5 == 0) and (numb % 7 != 0)) or ((numb % 5 != 0) and (numb % 7 == 0))


f = open('../test.txt')
lines = f.readlines()[1:]
f.close()
lcms = []
rasns = []
for k in tqdm(range(len(lines))):
    line = lines[k]
    nums = [int(i) for i in line.split(' ')[1:]]
    l = len(nums)
    lcml = []

    for i in range(l-1):
        for j in range(i+1, l):
            nok = lcm(nums[i], nums[j])
            if nok not in lcml:
                lcml.append(nok)
    lcml.sort(reverse=True)

    len_lcml = len(lcml)
    if len_lcml > 1:
        rasl = []
        maxn = lcml[0]
        for i in range(len_lcml):
            rasl.append(maxn - lcml[i])
        rasns.append(rasl)
    lcms.append(lcml)

res = 0
for i in lcms:
    res += max(i)

cur_rasn = 0

while is_good(res - cur_rasn) == False:



    cur_rasn = 1


print(res)
