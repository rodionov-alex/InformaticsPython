with open("24_3.txt") as f:
    print(max(list(map(len, f.readline().strip().replace('PR', 'P R').replace('RP', 'R P').split()))))
