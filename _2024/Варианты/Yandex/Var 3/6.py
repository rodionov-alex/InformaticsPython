from turtle import *

scale = 40
getscreen().xscale = scale
getscreen().yscale = scale
setup(1.0, 1.0)
tracer(0)
lt(90)

for _ in range(6):
    fd(7)
    rt(120)

up()
fd(3)
rt(90)
down()

for _ in range(8):
    fd(5)
    rt(90)

up()

for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x, y)
        dot(3, 'red')

update()
done()

# 30
