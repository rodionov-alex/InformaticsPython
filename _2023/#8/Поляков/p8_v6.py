# Сергей составляет семизначные десятичные числа, такие что 2-я и 3-я цифры числа представляют собой квадрат
# первой цифры, а перед последней цифрой числа записан куб последней цифры. Сколько подходящих чисел может
# составить Сергей?
#
# Ответ: 2925

count = 0
# Все возможные начала чисел: первая цифра + 2 цифры ее квадрата (от 1 т.к. число с 0 начинаться не может)
beginings = [str(x) + str(x * x).zfill(2) for x in range(1, 10)]
# Все возможные окончания чисел: куб последней цифры + сама последняя цифра
endings = [str(x * x * x) + str(x) for x in range(10)]

# Перебор начал
for begin in beginings:
    # Перебор окончаний
    for end in endings:
        # Для каждого сочетания начала и конца числа количество возможных семизначных чисел равно 10 в степени
        # недостающего до 7 знаков количества цифр (например 3 в начале и 2 в конце -> недостает 2 цифр)
        count += 10 ** (7 - len(begin) - len(end))

print(beginings)
print(endings)
print(count)
