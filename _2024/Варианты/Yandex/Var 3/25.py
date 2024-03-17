from fnmatch import fnmatch

count = 5
n = 5 ** 10

while n % 42:
    n -= 1

while count:
    if fnmatch(str(n), '48*15*0'):
        print(n, n // 42, sep='\t')
        count -= 1

    n -= 42
