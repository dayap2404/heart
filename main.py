import math
from turtle import *

def first_heart(x) :
    return 15 * math.sin(x) ** 3

def second_heart(y) :
    return 12 * math.cos(y) -5 * \
        math.cos(2 * y) - 2 * \
        math.cos(3 * y) - \
        math.cos(4 * y)

speed(100000)
bgcolor("black")

for i in range(6000) :
    goto(first_heart(i)*20, second_heart(i)*20)

    for j in range(5) :
        color("#f73487")

    goto(0,0)

done()