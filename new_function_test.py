__author__ = 'lyndsay.beaver'
import random
throws=5

def roll_dice():
    throw_1=random.randint(1,6)
    throw_2=random.randint(1,6)
    total=throw_1+throw_2
    rolls=[total, throw_1, throw_2]
    return rolls


def check_results(rolls):
    if rolls[0] == 7:
        #throw_count+=1
        #print('Count: ', i + 1)
        #point = 0
        print('You rolled a Seven!')
    elif rolls[0] == 2 or rolls[0] == 3 or rolls[0] == 12:
        #throw_count+=1
        #print('Count: ', i +1)
        #point=0
        print('You rolled craps', rolls[0])
    else:
        throw_status=1
        #print('Count: ', i+1)
        print('You set a point', rolls[0])
        point = rolls[0]


def main():
    check_results(roll_dice())

main()
