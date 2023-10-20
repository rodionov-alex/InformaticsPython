print('x', 'y', 'z', 'w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x and w) or (w and z)) == ((z<=y) and (y<=x))) == 1:
                    print(x, y, z, w)