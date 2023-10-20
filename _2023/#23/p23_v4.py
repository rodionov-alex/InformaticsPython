# Исполнитель преобразует число, записанное на экране. У исполнителя есть две команды, которым присвоены номера:
# 1. Вычти 3
# 2. Раздели нацело на 2
# Выполняя первую из них, исполнитель уменьшает число на экране на 3, выполняя вторую – делит число на экране на 2
# нацело, отбрасывая остаток. Программой для исполнителя называется последовательность команд. Сколько существует
# программ, для которых при исходном числе 108 результатом является число 12, и при этом траектория вычислений
# содержит число 42?
#
# Ответ: 30

# Функция поиска всех возможныъх траекторий
def f(a, b):
    if a == b:
        # Траектория завершена
        return 1
    elif a < b:
        # Неудача, траектория вышла за целевое число
        return 0
    else:
        # Рекурсивно продолжаем поиск
        return f(a - 3, b) + f(a // 2, b)


print('Ответ:', f(108, 42) * f(42, 12))
