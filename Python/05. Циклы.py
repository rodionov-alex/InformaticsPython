print('-=-=-= ЦИКЛ for =-=-=-')

# Цикл с заранее известным количеством повторений (итераций).
# В цикле for пишется в каком диапазоне значений изменяется i. Функция range() может принимать до 3 аргументов.
# Сигнатура функции выглядит следующим образом: range(<ОТ_включительно>, <ДО_не_включительно>, <шаг>). Если
# представить диапазон в виде математического интервала, то он быдет выглядеть так: [ОТ; ДО).
# По умолчанию <шаг> всегда равен 1, если его не указать в качестве аргумента. Так же, если не указать и
# аргумент <ОТ>, то по умолчанию он будет равен 0.

# i изменяется от 0 до 5
print('for i in range(5):')
for i in range(5):
    print(i)
print()

# i изменяется от 15 до 20
print('for i in range(15, 20):')
for i in range(15, 20):
    print(i)
print()

# i изменяется от 10 до 20 с шагом 2
print('for i in range(10, 20, 2):')
for i in range(10, 20, 2):
    print(i)
print()


print('-=-=-= ЦИКЛ while =-=-=-')

# Цикл while используется когда количество повторений (итераций) заранее неизвестно.
# После ключевого слова while пишется логическое выражение или "условие выполнения цикла".
# Как только это условие вернет значение 0 | False | Ложь, то цикл перестанет выполняться.

x = 11
print('x =', x)
x_2 = ''

while x > 0:
    x_2 = str(x % 2) + x_2
    x //= 2

print('x_2 =', x_2)
print()


print('-=-=-= ПРИНУДИТЕЛЬНОЕ ПРЕРЫВАНИЕ ЦИКЛОВ =-=-=-')

# При помощи операторов break и continue можно принудительно прервать выполнение цикла
# или пропустить его текущую итерацию. Эти операторы можно использовать как в цикле for,
# так и в цикле while.

a = 10

while True:  # Бесконечный цикл
    a += 1

    if a % 2 == 0:
        print('continue')
        continue

    if a > 20:
        print('break')
        break

    print(a)
print()


print('-=-=-= ЦИКЛ do_while ИЛИ repeat_until =-=-=-')

# Поскольку в питоне нет аналогов циклу do_while (C++) или repeat_until (Pascal), то реализуют
# его при помощи стандартного цикла while. Запускают бесконечный цикл while, затем идет обычное тело
# цикла в конце которого стоит условие выхода из цикла с оператором break. Таким образом имеем цикл while,
# тело которого выполнится минимум один раз.

a = 10

while True:
    print(a)
    a += 1

    if a >= 10:
        break
print()


print('-=-=-= БЛОК else В ЦИКЛАХ =-=-=-')

# В циклах в блок else управление передается в том случае, если выполнение цикла не прерывалось оператором break.
# Можно сказать, что блок else в цикле служит для обработки "безрезультатного" выполнения цикла. К примеру, если
# при помощи цикла в списке ищется какой-либо элемент. Если элемент найден, то цикл можно прервать оператором break
# так как элемент уже найден и дальнейший поиск будет бессмысленен. Но вот если элемент так и не был найден, то
# эту ситауцию нужно как то обработать, вывести сообщение например. В этом может помочь блок else в цикле: если
# элемент не найден и цикл не прерывался, то управление передается в блок else, где можно вывести сообщение об этом.

for i in range(10):
    if i == 11:
        print("Цикл прерван")
        break
else:
    print("Блок else в цикле")
