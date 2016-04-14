__author__ = 'lyndsay.beaver'
import math
import random

radius = 10
t = 2*math.pi*random.randint(0,5)
u = random.randint(0,5)+random.randint(0,5)
print("T is: ", t)
print("U is: ", u)
r = 0
if u > 1:
    r = 2-u
else:
    r = u
print("R is: ", r)