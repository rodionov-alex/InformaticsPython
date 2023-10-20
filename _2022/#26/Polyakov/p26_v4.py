with open('26_4.txt') as f:
    s = int(f.readline().split()[1])
    nums = list(map(int, f.readlines()))
    nums.sort()
    ships = [0]
    while len(nums):
        cargo = nums.pop()
        for i in range(len(ships)):
            if ships[i] + cargo <= s:
                ships[i] += cargo
                break
        else:
            ships.append(cargo)
    print(len(ships), ships[-1])
    