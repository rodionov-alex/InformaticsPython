from tqdm import tqdm

def is_simple(num):
    if num % 2 == 0:
        return False

    sqrt_d = int(num ** 0.5)

    for i in range(3, sqrt_d + 1, 2):
        if num % i == 0:
            return False

    return True

pairs = 0
avg = 0

for i in tqdm(range(3000001, 10000000, 2)):
    if is_simple(i) and is_simple(i+2):
        pairs += 1
        avg = i + 1

print(pairs, avg)
print('Finish')
