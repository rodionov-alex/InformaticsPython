# Для решения данной задачи используется правило, что если два числа имеют
# одинаковый остаток от деления на 43, то разность этих чисел будет
# кратна 43. Например 134 и 220: 134 % 43 = 5; 220 % 43 = 5; Остаток одинаковый;
# 220 - 134 = 86; 86 кратно 43 (86 % 43 = 0).

f = open('b.txt')
n = int(f.readline())  # Общее количество элементов

# Словарь с минимальными суммами; ключ - остаток от деления;
# В этот словарь добавляются только первые суммы, которые дают определенный остаток
# от деления (являющийся ключем), а так же индекс в последовательности, когда эта
# сумма была получена.
min_sums = {}

summa = 0       # Общая сумма
max_sum = 0     # Масимальня сумма элементов последовательности
min_len = 0     # Минимальная длина последовательности с максимальной суммой
cur_sum = 0     # Текущая сумма элементов последовательности
cur_len = 0     # Текущая длина последовательности

for i in range(n):
    # Общая сумма увеличивается с каждым считанным элементом
    summa += int(f.readline())
    # Остаток от деления на 43
    d = summa % 43
    # Если остаток равен 0, то суммма всех считанных элементов
    # будет кратна 43 и яляться максимальной
    if d == 0:
        max_sum = summa
        min_len = i
    else:
        # Если определенный остаток от деления на 43 встречается первый раз,
        # то его надо поместить в словарь min_sums, чтобы в будущем производить
        # от него рассчетсуммы и длины последовательности.
        if d not in min_sums.keys():
            min_sums[d] = (summa, i)
        # Если определенный остаток от деления на 43 уже есть в словаре, то
        # считаем сумму и длину последовательности.
        else:
            # Сумма последовательности кратная 43, это разность между двумя
            # суммами с одинаковыми остатками.
            cur_sum = summa - min_sums[d][0]
            # длина последовательности - это, соответственно, разность между
            # ткущим индексом, и индексом первой суммы с таким же остатком.
            cur_len = i - min_sums[d][1]
            # Если сумма получилась больше максимальной, или равна ей, но меньшей
            # длины, то необходимо обновить значения соответствующих переменных.
            if cur_sum > max_sum or (cur_sum == max_sum and cur_len < min_len):
                max_sum = cur_sum
                min_len = cur_len

f.close()
print(min_len)
