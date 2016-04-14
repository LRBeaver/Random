__author__ = 'lyndsay.beaver'
import random

def rolldice():

    init = int(0)
    rolls = []
    for i in range(0,3):
    #l.append(init + ( float(i) / 100 ))
        rolls += [init + (random.randint(1,6))]
    return rolls

def total(rolls):
    sum = 0
    for i in range(len(rolls)):
        sum += rolls[i]
    print "Roll is: ", sum

def main():
    times = 6
    for x in range(times):
        total(rolldice())

main()