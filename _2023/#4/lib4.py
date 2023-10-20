from itertools import permutations
from tqdm import tqdm

# Проверка условия Фано
def check_phano(values, phano):
    ln = len(values)

    # Прямое условие Фано
    if phano >= 0:
        for i in range(ln - 1):
            for j in range(i + 1, ln):
                if values[i].startswith(values[j]) or values[j].startswith(values[i]):
                    break
            else:
                continue
            break
        else:
            return True

    # Обратное условие Фано
    if phano <= 0:
        for i in range(ln - 1):
            for j in range(i + 1, ln):
                if values[i].endswith(values[j]) or values[j].endswith(values[i]):
                    break
            else:
                continue
            break
        else:
            return True

    return False


# Подсчет длины закодированного слова по словарю
def calc_length(wrd: str, dct: dict):
    res = 0

    for ch in wrd:
        res += len(dct[ch])

    return res


# Подсчет минимальной глубины проверки по количеству символов алфавита
def get_min_depth(cahrs_count: int):
    min_depth = 1

    while 2 ** min_depth < cahrs_count:
        min_depth += 1

    return min_depth


def ege_n4(word: str, alf: dict, phano: int = 1, all_results: int = 0, depth: int = 4):
    """
    Функция для решения четвертого задания ЕГЭ (условие Фано).
    :param word: кодируемое слово.
    :param alf: алфавит с текстовыми двоичными кодами символов (неизвестные коды должны быть пустыми).
    :param phano: >0 - прямое условие Фано, <0 - обратное условие Фано, =0 - оба.
    :param all_results: если равно 0, то вернуть только минимальное количество двоичных знаков, иначе вернуть все
    найденные подходящие последоватеьности.
    :param depth: глубина поиска, максимальное количество двоичных знаков на символ.
    :return: Возвращает минимальное количество двоичных знаков или все найденные подходящие последоватеьности.
    """

    result = []
    # Список известных кодов букв алфавита
    occupied = [alf[x] for x in alf if len(alf[x]) != 0]
    # Количество неизвестных букв алфавита
    unk_сhars = sum([1 for x in alf if len(alf[x]) == 0])
    # Определение минимальной глубины поиска относительно количества и кодов букв алфавита
    min_depth = max(get_min_depth(len(alf.keys())), max(list(map(len, alf.values()))))
    # Определение глубины поиска относительно желаемой и минимальной глубин
    depth = max(depth, min_depth)
    # Пул возможных значений для неизвестных букв алфавита значений
    val_pool = []
    # Заполнение пула возможных значений
    for x in range(2 ** depth):
        bx = bin(x)[2:]
        val_pool.append(bx)
        # Дополнить значениями до глубины поиска
        while len(bx) < depth:
            bx = '0' + bx
            val_pool.append(bx)

    # Перебор всевозможных перестановок из пула по количеству неизветных
    perm = list(permutations(val_pool, r=unk_сhars))

    for i in tqdm(range(len(perm))):
        comb = perm[i]
    # for comb in permutations(val_pool, r=unk_сhars):
        # Полученная комбинация значений для неизвестных проверяется по правилу Фано.
        # Отдается список известных + неизвестных
        if check_phano(occupied + list(comb), phano):
            # Копия словаря для проверки (чтобы не потерять оригинал)
            check_alf = alf.copy()
            # Заполнение словаря из комбинации
            for val in comb:
                for k in check_alf:
                    if len(check_alf[k]) == 0:
                        check_alf[k] = val
                        break

            # Подсчет длины закодированного слова
            result.append((calc_length(word, check_alf), check_alf))

    return min(result, key=lambda x: x[0]) if all_results == 0 else result
