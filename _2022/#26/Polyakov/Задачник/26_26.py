with open(r'26data/26-J1.txt') as f:
    baskets = list(map(int, f.readlines()[1:]))
    boxes = 0
    while len(baskets):
        residue = 100 - baskets.pop(0)
        if residue in baskets:
            baskets.remove(residue)
            boxes += 1
    print(boxes)