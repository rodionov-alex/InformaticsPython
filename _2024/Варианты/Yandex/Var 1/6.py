from turtle import *

scale = 50
getscreen().xscale = scale
getscreen().yscale = scale
setup(1.0, 1.0)
tracer(0)
lt(90)

rt(60)
fd(4)
rt(120)

for i in range(4):
    fd(3)
    rt(240)
    fd(3)
    rt(120)

fd(4)
rt(90)
fd(8 * 3 ** 0.5)
rt(90)
fd(8)

up()

print(78)

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x, y)
        dot(3, 'red')

update()
done()