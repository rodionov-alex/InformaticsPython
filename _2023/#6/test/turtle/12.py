from turtle import *

setup(1.0, 1.0)
tracer(0)
ht()
lt(90)
scale = 1.0
count = 0

scr = getscreen()
scr.xscale = scale
scr.yscale = scale

color("black", "lightgreen")
cnv = getcanvas()

begin_fill()
for i in range(4):
    rt(90)
    fd(50)
end_fill()
up()

for x in range(-200, 200):
    for y in range(-200, 200):
        # goto(x, y)
        # dot(1, 'red')
        items = cnv.find_overlapping(x, y, x, y)

        if len(items) == 1 and items.count(5) > 0:
            count += 1

update()
#exitonclick()
print(count)
