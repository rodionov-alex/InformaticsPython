# Автор: Е. Драчева

from itertools import combinations

def gcd( a, b ):
    while a and b:
        a, b = b, a % b
    return a + b

f = open('27-77a.txt')
n = int(f.readline())

s = [0]

for _ in range(n):
    mas = [int(x) for x in f.readline().split()][1:]
    pair_nok = []
    for p in combinations(mas, 2):
        pair_nok.append( (p[0]*p[1]) // gcd(p[0],p[1]) )
    print( 'NOK:', sorted(pair_nok) )
    cmb = [a+b for a in s for b in pair_nok]
    sorted_cmb = sorted(cmb)
    s = { x % 35: x for x in sorted_cmb }.values()
    print( sorted(s) )

f.close()
print( [x for x in s if (x % 5 == 0) != (x % 7 == 0)] )
m = max( x for x in s if (x % 5 == 0) != (x % 7 == 0) )
print( m )
