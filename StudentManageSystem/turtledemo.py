import turtle as t

t.setup(800,600,200,200)
t.penup()

t.pencolor('purple')
t.fd(-250)
t.pendown()
t.pensize(20)
t.seth(-40)
for i in range(4):
    t.circle(40,80)
    t.circle(-40,80)
t.circle(40,80/2)
t.fd(40)
t.circle(16,180)
t.fd(40*2/3)

t.done()