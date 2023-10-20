from turtle import *

setup(1.0, 1.0)
tracer(0)
ht()
lt(90)
scale = 1.0
count1 = 0
count2 = 0

scr = getscreen()
scr.xscale = scale
scr.yscale = scale

color("black", "lightgreen")
begin_fill()
for i in range(3):
    lt(60)
    fd(300)
    lt(60)
end_fill()

up()
cnv = getcanvas()

for x in range(-300, 300):
    for y in range(-300, 300):
        item = cnv.find_overlapping(x, y, x, y)

        if len(item) == 1 and item[0] == 5:
            count1 += 1


for x in range(-259, 1):
    for y in range(-149, 149):
        if y < -x / 3 ** 0.5 + 150 and y > x / 3 ** 0.5 - 150:
            count2 += 1

update()
# exitonclick()
print(count1, count2)
