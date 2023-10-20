print('x', 'y', 'z', 'w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((z and y) or ((x <= z) == (y<=w))) == 0:
                    print(x, y, z, w)