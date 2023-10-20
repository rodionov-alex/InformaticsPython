from turtle import *

s = 30
setup(1.0, 1.0)
getscreen().xscale = s
getscreen().yscale = s
tracer(0)
lt(90)

for _ in range(2):
    fd(10)
    rt(90)
    fd(20)
    rt(90)

up()
fd(5)
rt(90)
fd(7)
lt(90)
down()

for _ in range(2):
    fd(20)
    rt(90)
    fd(40)
    rt(90)

up()

for x in range(-10, 30):
    for y in range(-10, 30):
        goto(x, y)
        dot(3, 'red')

done()
