print('x', 'y', 'z', 'w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                t = not y and z
                if (x and (y or (not z)) and w) == (x == t or t):
                    print(x, y, z, w)
