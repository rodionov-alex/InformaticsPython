import re

s = 'qwe/rtyqwe/rtyqwe/rtyqwe/rty 77 456'

print(re.findall(r'qwe', s))  # находит все qwe в строке s
print(re.match(r'qwe', s))  # ищет qwe в начале строки
print(re.search(r'rty', s))  # ищет rty во всей строке
print(re.fullmatch(r'qwe', s))  # производит проверку строки s на полное соответствие шаблону
print(re.split(r'rty', s))  # Разделяет строку на подстроки по подстрокам соответствующим шаблону
print(re.sub(r'qwe', 'rty', s))  # Заменяет последовательности соответствующие шаблону на rty

res = re.search(r'\d\d\d', s)
res = re.search(r'\D\D\D', s)

# . - любой символ
# ? - 0 или 1
# * - от 0 до inf
# + - от 1 до inf

res = re.search(r'\d*', s)
res = re.search(r'[A-Za-z]+', s)
res = re.search(r'[yt]+', s)
res = re.search(r'.[rt]+', s)
res = re.search(r'\d{2,3}', s)




print(res)

