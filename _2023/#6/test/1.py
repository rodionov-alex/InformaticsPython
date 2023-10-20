from turtle import *

# Посчитать количество отрезков.

tracer(0)
setup(1.0, 1.0)
scale = 10

for i in range(100):
    fd(10 * scale)
    right(30)

update()
exitonclick()

# Ответ 12