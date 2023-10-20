from turtle import *

# Посчитать количество целочисленных координат на

scale = 15
setup(1.0, 1.0)
tracer(0)

for i in range(10):
    fd(15 * scale)
    right(60)

up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * scale, y * scale)
        dot(5, "blue")

update()
exitonclick()

# Ответ 32, не сошелся (16)