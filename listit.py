__author__ = 'lyndsay.beaver'
import random

init = int(0)
numitems = 6
l = []
for i in range(numitems):
    #l.append(init + ( float(i) / 100 ))
    l += [init + (random.randint(1,6))]
print l