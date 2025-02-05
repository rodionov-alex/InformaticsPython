# Григорий составляет 16-буквенные слова из букв А, Н, Т, И, У, О, П, Я, выбирая такие, в которых содержится
# комбинация АНТИУТОПИЯ. Сколько слов сможет составить Григорий?
#
# Ответ: 1835008

# Так как слова имею длину 16 а алфавит состоит из 8 букв, то перебором программа будет проверять 8^16 слов.
# Это порядка 281 474 976 710 656 слов.

# 1. АНТИУТОПИЯ______
# 2. _АНТИУТОПИЯ_____
# 3. __АНТИУТОПИЯ____
# 4. ___АНТИУТОПИЯ___
# 5. ____АНТИУТОПИЯ__
# 6. _____АНТИУТОПИЯ_
# 7. ______АНТИУТОПИЯ
# Всего 7 возможных положений подстроки. Количество слов для каждого положения рассчитывается следующим образом:
# Всего имеем 6 мест для других букв алфавита. Таким образом количество возможных комбинаций равно
# 8^6 = 262144. Это количество комбинаций на одно положение подстроки, а всего таких положений 7, поэтому
# 262144 * 7 = 1835008 слов.
