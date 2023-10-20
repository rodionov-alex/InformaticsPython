f = open('17_1.txt')
lines = f.readlines()
f.close()
nums = [int(n) for n in lines]  # Список чисел
nums_count = len(nums)          # Количество чисел
sums = []                       # Суммы троек

# Перебор чисел
for i in range(nums_count - 2):
    triple = nums[i:i+3]  # Тройка чисел

    # Проверка тройки на уникальность по следующим условиям:
    # - первое число может быть любым, кроме положительного числа, заканчивающегося на 9
    # - второе число тройки может быть только положительным числом, заканчивающимся на 9
    # - третье число может быть любым, кроме положительного числа, заканчивающегося на 9
    if (not (triple[0] > 8 and triple[0] % 10 == 9)) and \
        (triple[1] > 8 and triple[1] % 10 == 9) and \
       (not (triple[2] > 8 and triple[2] % 10 == 9)):
        sums.append(sum(triple))

print(len(sums), max(sums))
