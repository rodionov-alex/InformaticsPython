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

begin_fill()
p = position()
goto(p[0] + 200, p[1] + 100)
p = position()
goto(p[0] - 50, p[1] - 150)
p = position()
goto(p[0] - 150, p[1] + 50)
end_fill()

#up()
cnv = getcanvas()

for x in range(0, 210):
    for y in range(-100, 110):
        item = cnv.find_overlapping(x, y, x, y)
        # goto(x, y)
        # dot(2, "red")

        if len(item) == 1 and item[0] == 5:
            count += 1

print(count)
update()
#exitonclick()