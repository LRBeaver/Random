__author__ = 'lyndsay.beaver'
import random

def rolldice():
    roll = (random.randint(1,20))
    print "To hit, you rolled a: ", roll
    if roll == 20:
        print "    Possible critical!"
        secondhit = (random.randint(1,20))
        if secondhit == 20:
            print "       You critted!!"
            critdamage()
        else:
            print "Normal damage"
    else:
        print "      Rolling hit"
        hit(roll)
    return roll


def hit(roll):

    if roll >= 12 and roll < 20:
        print "It's a hit!"
        print "      Rolling damage"
        damage()
    else:
        print "Miss"

def critdamage():
    critdmg = (random.randint(1,6))
    print "The critical damage was:", critdmg
    print "Doubled, thats: ", critdmg * 2
    return critdmg

def damage():
    dmg = (random.randint(1,6))
    print "The damage was:", dmg
    return dmg

def total(rolls):
    sum = 0
    #for i in range(len(rolls)):
        #sum += rolls[i]
    print "Roll is: ", sum

def main():
    #times = 6
    #for x in range(times):
    rolldice()

main()