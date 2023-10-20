f = open('17_19.txt')
lines = f.readlines()
f.close()
nums = [int(n) for n in lines]  # Список чисел
nums_count = len(nums)          # Количество чисел
sums = []                       # Список сумм пар элементов заканчивающихся на 5

# Перебор чисел
for i in range(nums_count - 1):
    # Если пара чисел заканчивается на пятёрки, то добавить их сумму в список
    if nums[i] % 10 == 5 and nums[i + 1] % 10 == 5:
        sums.append(nums[i] + nums[i + 1])

# Вывод количества сумм и максимальной из них
print(len(sums), max(sums))
