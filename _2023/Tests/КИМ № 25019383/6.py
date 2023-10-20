import turtle as t

scale = 30

t.setup(1.0, 1.0)
t.getscreen().xscale = scale
t.getscreen().yscale = scale
t.ht()
t.tracer(0)
t.lt(90)

for i in range(6):
    t.fd(5)
    t.rt(60)

t.up()
t.fd(5)
t.rt(90)
t.down()

for j in range(2):
    t.fd(15)
    t.rt(90)
    t.fd(5)
    t.rt(90)

t.up()

for x in range(-20, 20):
    for y in range(-20, 20):
        t.goto(x, y)
        t.dot(3, 'red')

t.done()
