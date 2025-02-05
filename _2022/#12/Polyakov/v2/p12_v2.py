# s = '111113'  # Res = 222223 | Sum = 13
# s = '133333'  # Res = 233333 | Sum = 16

# Видно, что в результате работы алгоритма единицы меняются на двойки, а самой маленькой будет сумма в строке
# состоящей только из одних единиц и одной тройки. Это значит что для результата 404 такая трока будет самой длинной.
# Заметим , что если на конце одна тройка, то сумма будет нечетной, поэтому на конце должны быть две тройки, чтобы
# сумма была четной. Итого получим: 404 - 2 * 3 = 398; 398 / 2 = 199; 199 единиц должно быть в строке
# Ответ: 199 единиц + 2 тройки = 201 символ

s = '1' * 199 + '33'

print(s)

while ('12' in s) or ('13' in s):
    s = s.replace('12', '21', 1)
    s = s.replace('31', '23', 1)
    s = s.replace('13', '23', 1)

print(s)

sum_s = 0

for c in s:
    sum_s += int(c)

print('Sum = ', sum_s)

print('Len = ', len(s))
