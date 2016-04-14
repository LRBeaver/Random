__author__ = 'lyndsay.beaver'
import random

times = 6

def randomization():
    number=random.randint(1,6)
    roll = number*3
    return number, roll

for number in range(times): #range(random.randint(1,10)):
    print randomization()