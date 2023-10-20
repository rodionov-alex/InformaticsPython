with open('24data/24-203.txt') as f:
    text = f.readline()
    length = len(text)
    last_ind = length - 1
    min_substr_size = 3

    no_a_ind = -1  # Индекс начала подстроки без A
    no_b_ind = -1  # Индекс начала подстроки без B
    no_c_ind = -1  # Индекс начала подстроки без C

    sub_strings = []  # Индексы подстрок не менее минимальной длины

    for i in range(length):
        if text[i] == 'A':
            if no_a_ind >= 0:
                # Построка подходящей длины
                if i - no_a_ind >= min_substr_size:
                    sub_strings.append((no_a_ind, i - 1))
                # Сброс начального индекса
                no_a_ind = -1
            if no_b_ind < 0:
                no_b_ind = i
            if no_c_ind < 0:
                no_c_ind = i
        if text[i] == 'B':
            if no_a_ind < 0:
                no_a_ind = i
            if no_b_ind >= 0:
                # Построка подходящей длины
                if i - no_b_ind >= min_substr_size:
                    sub_strings.append((no_b_ind, i - 1))
                # Сброс начального индекса
                no_b_ind = -1
            if no_c_ind < 0:
                no_c_ind = i
        if text[i] == 'C':
            if no_a_ind < 0:
                no_a_ind = i
            if no_b_ind < 0:
                no_b_ind = i
            if no_c_ind >= 0:
                # Построка подходящей длины
                if i - no_c_ind >= min_substr_size:
                    sub_strings.append((no_c_ind, i - 1))
                # Сброс начального индекса
                no_c_ind = -1
        # Когда дошли до конца - необходимо проверить все подстроки
        if i == last_ind:
            if no_a_ind >= 0 and i + 1 - no_a_ind >= min_substr_size:
                sub_strings.append((no_a_ind, i))
            if no_b_ind >= 0 and i + 1 - no_b_ind >= min_substr_size:
                sub_strings.append((no_b_ind, i))
            if no_c_ind >= 0 and i + 1 - no_c_ind >= min_substr_size:
                sub_strings.append((no_c_ind, i))

    # Все возможные подстроки в виде кортежей (индекс_начала, индекс_конца)
    # set() исключает повторения
    all_subs = set()

    # Перебор всех возможных подстрок среди найденных
    for w in sub_strings:
        for i in range(w[0], w[1] - 1):
            for j in range(i + 2, w[1] + 1):
                all_subs.add((i, j))

    print(len(all_subs))


