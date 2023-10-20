import turtle as t

scale = 30
t.setup(1.0, 1.0)
t.getscreen().xscale = scale
t.getscreen().yscale = scale
t.tracer(0)
t.ht()
t.lt(90)

for i in range(4):
    t.fd(10)
    t.rt(90)

t.rt(30)

for i in range(5):
    t.fd(6)
    t.rt(60)
    t.fd(6)
    t.rt(120)

t.up()

for x in range(-20, 20):
    for y in range(-20, 20):
        t.goto(x, y)
        t.dot(3, 'red')

t.done()

# Ответ: 51
