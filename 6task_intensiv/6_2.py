from turtle import *

screensize(5000,5000)
tracer(0)
k = 20

down()
forward(9*k)
right(90)
for _ in range(2):
    forward(3*k)
    right(90)
    forward(3*k)
    right(270)
for _ in range(2):
    forward(3*k)
    right(90)
forward(9*k)
up()

for y in range(-30, 30):
    for x in range(-30, 30):
        goto(x*k, y*k)
        dot(5)
done()