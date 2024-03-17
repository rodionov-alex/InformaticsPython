from turtle import *

scale = 30

getscreen().xscale = scale
getscreen().yscale = scale
setup(1.0, 1.0)
tracer(0)
lt(90)

for _ in range(7):
    fd(10)
    rt(120)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x, y)
        dot(3, 'red')

done()

# Ответ: 38
