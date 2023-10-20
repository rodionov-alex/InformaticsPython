from turtle import *

# Посчитать количество точек внутри фигуры.

scale = 40
setup(1.0, 1.0)
tracer(0)

for i in range(7):
    fd(10 * scale)
    rt(120)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * scale, y * scale)
        dot(5, "red")

update()
exitonclick()

# Ответ 38