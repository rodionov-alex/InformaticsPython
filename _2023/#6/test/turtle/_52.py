from turtle import *

setup(1.0, 1.0)
tracer(0)
ht()
lt(90)
s = 2
count = 0

begin_fill()
for i in range(3):
    lt(60)
    fd(300 * s)
    lt(60)
end_fill()

cnv = getcanvas()

for x in range(-250 * s, 10 * s, s):
    for y in range(-160 * s, 160 * s, s):
        it = cnv.find_overlapping(x, y, x, y)

        if len(it) == 1:
            count += 1

print(count)