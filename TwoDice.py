__author__ = 'lyndsay.beaver'
import random
point = 0
throw_status=0
if throw_status==0:
   for i in range (6):
       throw_1=random.randint(1,6)
       throw_2=random.randint(1,6)
       total = throw_1 + throw_2
       print('--------------')
       print(total)
       print('Throw 1: ', throw_1)
       print('Throw 2: ', throw_2)
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
else:
    print('This was the next throw', throw_status)