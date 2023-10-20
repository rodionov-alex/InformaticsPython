# Текстовый файл 24-203.txt содержит строку из заглавных латинских букв A, B и C, всего не более чем из 10^6 символов.
# Определите количество подстрок длиной не менее трех символов, которые не содержали бы одновременно все три буквы A,
# B и C. Примечание: подстрока — это непрерывный фрагмент исходной строки.
#
# Ответ: 252776

# Подсчет количества подстрок миниамльной длины 3 у строки длиной n
def count_subs(n):
    res = 0

    for i in range(1, n - 3 + 2):
        res += i

    return res

with open('24-203.txt') as f:
    s = f.readline().strip()
    sub_str = s[0]
    s = s[1:]
    count = 0           # Общее количество подстрок
    double_counted = 0  # Количество подстрок которые считаются дважды

    # Например для строки АААВВВССС есть две больших подстроки стреди которых считаются подходящие подстроки.
    # Это АААВВВ и ВВВССС, при этом подходящая комбинация ВВВ будет учтена дважды, в первой подстроке и второй.
    # Чтобы изавляться от подсчета таких дубликатов используется переменная double_counted.

    # Пребор всех символов
    for ch in s:
        # Если символ уже присутствует в подстроке или в подстроке только один вид символов
        if ch in sub_str or len(set(sub_str)) == 1:
            # то просто добавить новый символ в подстроку
            sub_str += ch
        # В противном случае
        else:
            # Произвести подсчет комбинаций
            if len(sub_str) >= 3:
                # Текущее количество подстрок минус количество дубликатов предыдущего подсчета
                count += count_subs(len(sub_str)) - double_counted

            # Обрезка строки так, чтобы остались только последние одинаковые символы
            new_str = ''
            last = sub_str[-1]

            while sub_str[-1] == last:
                new_str += last
                sub_str = sub_str[:-1]

            # Подсчет дубликатов
            double_counted = count_subs(len(new_str))
            # Перезапишем sub_str как обрезок + новый символ
            sub_str = new_str + ch

    # Подсчет последней подстроки
    if len(sub_str) >= 3:
        count += count_subs(len(sub_str)) - double_counted

    print(count)
