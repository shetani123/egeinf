from turtle import *
screensize(5000,5000)
tracer(0)
k = 20

down()
for _ in range(4):
    forward(19*k)
    right(90)
    forward(30*k)
    right(90)
up()
forward(2*k)
right(90)
forward(8*k)
left(90)
down()
for _ in range(4):
    forward(93*k)
    right(90)
    forward(97*k)
    right(90)
up()
for y in range(-50,50):
    for x in range(-50,50):
        goto(x*k,y*k)
        dot(3)
done()