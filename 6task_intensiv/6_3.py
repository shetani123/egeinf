from turtle import *

screensize(5000,5000)
tracer(0)
k = 20

down()
for _ in range(2):
    forward(24*k)
    right(90)
    forward(16*k)
    right(90)
up()
for _ in range(10):
    right(90)
    forward(8*k)
    left(90)
down()
for _ in range(2):
    forward(15*k)
    right(90)
    forward(28*k)
    right(90)
up()
for y in range(-30,30):
    for x in range(-30,30):
        goto(x*k,y*k)
        dot(5)
done()