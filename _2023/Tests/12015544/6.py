from turtle import *

setup(1.0, 1.0)
scale = 30
getscreen().xscale = scale
getscreen().yscale = scale
tracer(0)
lt(90)
ht()

for i in range(5):
    fd(8)
    rt(60)
    fd(8)
    rt(120)

up()

for x in range(-15, 15):
    for y in range(-15, 15):
        goto(x, y)
        dot(3, 'red')

done()