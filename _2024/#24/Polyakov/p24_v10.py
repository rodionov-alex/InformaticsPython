def replace(line: str, st: str, ch: str):
    stch = st + ch
    while stch in line:
        ind = line.find(stch)
        ct = 1
        while line[ind - 1] == st:
            ind -= 1
            ct += 1
        line = line[:ind] + ch + st * ct + line[ind + ct + 1:]
    return line

with open('Files/24-204.txt') as f:
    s = f.readline().strip().replace('B', ' ').replace('AA', '*').replace('CC', '#')
    mx = max(map(len, s.replace('A', ' ').replace('C', ' ').split()))
    mx = max(mx, max(map(len, replace(s, '*', 'A').replace('A', ' ').replace('C', ' ').split())))
    mx = max(mx, max(map(len, replace(s, '#', 'C').replace('A', ' ').replace('C', ' ').split())))
    mx = max(mx, max(map(len, replace(replace(s, '*', 'A'), '#', 'C').replace('A', ' ').replace('C', ' ').split())))
    print(mx)

# w = 'C****AC'
# print(replace(w, '*', 'A'))
