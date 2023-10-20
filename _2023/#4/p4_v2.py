# По каналу связи передаются сообщения, содержащие только семь букв: П, Р, А, В, И, Л, О; для передачи
# используется двоичный код, допускающий однозначное декодирование (удовлетворяющий прямому или обратному
# условию Фано). Буквы П, А, Р имеют коды 1011, 01 и 0011 соответственно. Укажите наименьшую возможную
# длину закодированной последовательности для слова ПОВРАЛИПОПРАВО.
#
# Ответ: 42

from lib4 import ege_n4

word = 'ПОВРАЛИПОПРАВО'
alf = dict.fromkeys('ПРАВИЛО', '')
alf['П'] = '1011'
alf['А'] = '01'
alf['Р'] = '0011'

print(ege_n4(word, alf, 0))