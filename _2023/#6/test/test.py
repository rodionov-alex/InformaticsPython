import turtle as t

# Посчитать количество точек внутри фигуры.

count = 0
scale = 100

t.setup(1.0, 1.0)
t.tracer(0)
t.lt(90)
t.color("black", "lightgreen")

t.begin_fill()
for i in range(3):
    t.fd(10 * scale)
    t.rt(120)
t.end_fill()

# t.up()
#
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         t.goto(x * scale, y * scale)
#         t.dot(5, "blue")

canvas = t.getcanvas()

for y in range(-20, 20):
    for x in range(-20, 20):
        items = canvas.find_overlapping(x * scale, y * scale, x * scale, y * scale)

        if len(items) == 1:
            count += 1

t.update()
t.exitonclick()

print(count)

# Ответ 38