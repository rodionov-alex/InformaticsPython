with (open('24_12111.txt') as f):
    s = f.readline().replace('HPY', '*').replace('NYN', '*')
    s = s.replace('H', ' ').replace('N', ' ').replace('P', ' ').replace('Y', ' ')
    print(max(list(map(len, s.split()))))



