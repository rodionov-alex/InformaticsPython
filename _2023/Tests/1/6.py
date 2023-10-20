import turtle as t

t.tracer(0)
t.setup(1.0, 1.0)
scale = 30

t.getscreen().xscale = scale
t.getscreen().yscale = scale

t.left(90)

for i in range(7):
    t.fd(10)
    t.rt(120)

t.up()

for x in range(-10, 20):
    for y in range(-10, 20):
        t.goto(x, y)
        t.dot(5, 'red')

t.done()
