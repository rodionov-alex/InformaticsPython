from turtle import *

# Посчитать количество точек внутри фигуры и на линиях.

scale = 30
setup(1.0, 1.0)
tracer(0)

for i in range(16):
    left(36)
    fd(4 * scale)
    left(36)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * scale, y * scale)

        if x == y == 0:
            dot(3, "red")
        else:
            dot(3, "blue")


update()
exitonclick()

# Ответ 31
