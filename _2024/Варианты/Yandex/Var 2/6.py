from turtle import *

scale = 25
getscreen().xscale = scale
getscreen().yscale = scale
setup(1.0, 1.0)
tracer(0)
lt(90)
up()

rt(30)
fd(4)
rt(330)
down()
fd(4)
rt(90)
fd(7)
rt(45)
fd(4 * 2 ** 0.5)
rt(135)
fd(11)

up()
for x in range(20):
    for y in range(20):
        goto(x, y)
        dot(3, 'red')

update()
done()

# 38
