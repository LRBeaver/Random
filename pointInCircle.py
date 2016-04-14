__author__ = 'lyndsay.beaver'
import math
import random

def getRandomPointInCircle(radius):
    t = 2*math.pi*random.randint(0,5)
    u = random.randint(0,5)+random.randint(0,5)
    r = 0
    if u > 1:
        r = 2-u
    else:
        r = u
    print("T is: ", t)
    print("U is: ", u)
    print("This X,Y of the point is: ", radius*r*math.cos(t), radius*r*math.sin(t))

def roundm(n,m):
    n=1
    m=5
    print("this is the floor: ", math.floor(((n + m - 1)/m))*m)

def main():
    getRandomPointInCircle(10)
    roundm(1,5)

main()