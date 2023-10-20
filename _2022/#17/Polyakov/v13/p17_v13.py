f = open('17_13.txt')
lines = f.readlines()
f.close()
nums = [int(n) for n in lines]  # Список чисел
results = []                    # Список результатов

# Перебор всех чисел
for num in nums:
    n = num         # Копия числа для поиска суммы цифр
    digits_sum = 0  # Сумма цифр

    # Суммирование цифр
    while n != 0:
        digits_sum += n % 10
        n //= 10

    # Если сумма цифр делится на 3, то добавить в список результатов
    if digits_sum % 3 == 0:
        results.append(num)

# Вывод количества чисел и максимального из них
print(len(results), max(results))
