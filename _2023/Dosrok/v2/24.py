with open('24_7624.txt') as f:
    print(max(list(map(len, f.readline().strip().replace('XY', 'X Y').replace('YX', 'Y X') \
                                                .replace('XZ', 'X Z').replace('ZX', 'Z X') \
                                                .replace('YZ', 'Y Z').replace('ZY', 'Z Y') \
                                                .replace('XX', 'X X').replace('YY', 'Y Y') \
                                                .replace('ZZ', 'Z Z').split()))))
    