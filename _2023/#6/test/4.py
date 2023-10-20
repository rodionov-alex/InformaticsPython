from turtle import *

# Сколько раз черепаха пройдет через начало координат? (начальное положение не в счет)

tolerance = 10 ** -6  # Допустимое отклонение
scale = 10
count = 0
setup(1.0, 1.0)
tracer(0)

for i in range(151):
    forward(10 * scale)
    right(300)
    forward(20 * scale)
    right(300)
    pos = position()

    if abs(pos[0]) <= tolerance and abs(pos[1]) <= tolerance:
        count += 1

up()
goto(0, 0)
dot(5, "red")

update()
print(count)
exitonclick()

# Ответ 50
