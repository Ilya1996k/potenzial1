from turtle import  *
from random import randint
tracer(1)
screensize(3000,3000)
left(90)
up()
backward(300)
u = [20,30,40,35,25,15]
d=[50,100,80,30,120,110,70,25,90]
c=['#008000', '#00a550', '#33ff33','#007539','#004d20', '#90ee90', '#27a327']
def f(n):
    ugol = u[randint(0,len(u)-1)]
    pensize(n*5)
    if 1<n<6:
        color(c[randint(0, len(c) - 1)])
        dot(d[randint(0, len(d) - 1)])
        color('#964b00')

    if n ==0:
        color(c[randint(0,len(c)-1)])
        dot(d[randint(0,len(d)-1)])
        color('#964b00')
        return
    left(ugol)
    forward(30*n)
    f(n-1)
    pensize(n * 5)
    backward(30*n)
    right(ugol*2)
    forward(30 * n)
    f(n - 1)
    pensize(n * 5)
    backward(30 * n)
    left(ugol)

down()
color('#964b00')

n=7
pensize((n+1)*5)
forward(30*(n+1))
f(n)

done()
