f = open(r'F:\Informatics\Python\Mine\#24\v4\24.txt')
maxX = 0

for line in f:
    n = 1
    while 'X' * n in line:
        n += 1

    n -= 1
    
    if n > maxX:
        maxX = n

print(maxX)