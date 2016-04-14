__author__ = 'lyndsay.beaver'
import random
#total = 0
throws=5

def roll_dice():
    #for i in range(throws):
    throw_1=random.randint(1,6)
    throw_2=random.randint(1,6)
    global total=throw_1+throw_2
    #return total, throw_1, throw_2
    print(total, throw_1, throw_2)
print(roll_dice())

def check_results(total):
    if total == 7:
        #throw_count+=1
        print('Count: ', i + 1)
        point = 0
        print('You rolled a Seven!')
    elif total == 2 or total == 3 or total == 12:
        #throw_count+=1
        print('Count: ', i +1)
        point=0
        print('You rolled craps')
    else:
        throw_status=1
        print('Count: ', i+1)
        print('You set a point', total)
        point = total
print(check_results())