# В исследовательской лаборатории проводится наблюдение за солнечной активностью. Раз в год данные о наблюдениях
# записываются в базу данных с использованием минимально возможного целого числа байт. Первая часть данных включает
# в себя результат измерений, состоящий из 5-ти заглавных латинских букв (в латинском алфавите 26 символов). Вторая
# часть – год измерения (числа от 2000 до 2099 включительно). При этом используется посимвольное кодирование, каждый
# символ как результата, так и года, записывается с использованием минимально возможного числа бит. Сколько байтов
# требуется для хранения результатов всех измерений?
#
# Ответ: 500

# Первая часть. Для кодирования алфавитом из 26 букв потребуется 5 бит (2^5 = 32) на каждый символ.
# Всего 5 символов, стало быть 5 * 5 = 25 бит на первую часть.
# Вторая часть. Для кодирования года во второй части используются только цифры (10 цифр), при чем первые две
# цифры всегда статичны и равны 20, а значит их кодировать не нужно. Для кодирования 10 цифр необходимо 4 бита
# памяти, всего 2 цифры, таким образом 2 * 4 = 8 бит.

# В сумме первая и вторая части будут заниамть в памяти 25 + 8 = 33 бита или 5 байт.
# Всего начиная с 2000 и по 2099 данные будут записаны 100 раз. Это 5 * 100 = 500 байт.

