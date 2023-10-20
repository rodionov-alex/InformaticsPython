import turtle as t

t.tracer(0)
t.left(90)
scale = 30
t.getscreen().xscale = scale
t.getscreen().yscale = scale
t.ht()

for i in range(12):
    t.rt(60)
    t.fd(1)
    t.rt(60)
    t.fd(1)
    t.rt(270)

t.up()

for x in range(-10, 10):
    for y in range(-10, 10):
        t.goto(x, y)
        t.dot(5, 'red')

t.done()
