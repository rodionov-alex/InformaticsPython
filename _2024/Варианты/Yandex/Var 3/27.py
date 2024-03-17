from itertools import combinations

def fa(file):
    with open(file) as f:
        money = int(f.readline())
        products_count = int(f.readline())
        products = sorted([tuple(map(int, x.split())) for x in f])
        mx = 0
        res = []

        for i in range(2, products_count):
            combs = list(combinations(products, r=i))

            for comb in combs:
                if sum([x[0] for x in comb]) <= money:
                    sm = sum([x[1] for x in comb])
                    if mx < sm:
                        res = comb
                        mx = sm

        print(res)
        return mx

    return 0


def get_calories(bag, shop, money_left, mx_calories):
    calories = mx_calories
    bag_cost = sum([x[0] for x in bag])

    for prod in shop:
        if bag_cost + prod[0] <= money_left:
            bag.append()




def f(file):
    with open(file) as f:
        money = int(f.readline())
        products_count = int(f.readline())
        products = sorted([tuple(map(int, x.split())) for x in f])
        return get_calories([], products, money, 0)

    return 0

print(fa('27_A.txt'))
print(f('27_A.txt'))
# print(f('27_B.txt'))