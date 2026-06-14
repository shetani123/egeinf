from turtle import *

screensize(5000,5000)
tracer(0)
k = 10

down()
for _ in range(9):
    forward(22*k)
    right(90)
    forward(6*k)
    right(90)
up()
forward(1*k)
right(90)
forward(5*k)
left(90)
down()
for _ in range(9):
    forward(53*k)
    right(90)
    forward(75*k)
    right(90)
up()
for y in range(-50,50):
    for x in range(-50,50):
        goto(x*k,y*k)
        dot(2)
done()