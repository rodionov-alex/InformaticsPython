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


f = open('../27_1a.txt')
lines = f.readlines()[1:]
f.close()
lcms = []
for k in range(len(lines)):
    line = lines[k]
    nums = [int(i) for i in line.split(' ')[1:]]
    l = len(nums)
    lcml = []

    for i in range(l-1):
        for j in range(i+1, l):
            nok = lcm(nums[i], nums[j])
            if nok not in lcml:
                lcml.append(nok)

    lcms.append(lcml)

s = [0]
for i in tqdm(lcms):
    cmb = {a+b for a in s for b in i}
    s = {x for x in cmb}
    #print(s)
    
m = max(x for x in s if (x % 5 == 0) != (x % 7 == 0))

#print(m == 1254402115)
print(m)