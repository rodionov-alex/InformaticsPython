from turtle import *

scale = 25

getscreen().xscale = scale
getscreen().yscale = scale
setup(1.0, 1.0)
tracer(0)
lt(90)

for _ in range(2):
    fd(8)
    rt(90)
    fd(18)
    rt(90)

up()
fd(4)
rt(90)
fd(10)
lt(90)
down()

for _ in range(2):
    fd(17)
    rt(90)
    fd(7)
    rt(90)

up()

for x in range(0, 30):
    for y in range(0, 30):
        goto(x, y)
        dot(3, 'red')

done()

# Ответ: 275
