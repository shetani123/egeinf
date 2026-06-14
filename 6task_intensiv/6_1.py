from turtle import *

screensize(10000,10000)
tracer(0)
left(90)
k = 20
down()
right(30)
for _ in range(3):
    right(150)
    forward(6*k)
    right(30)
    forward(12*k)
up()

for y in range(-30, 30):
  for x in range(-30, 30):
    goto(x*k, y*k)
    dot(5, 'red')


done()