__author__ = 'lyndsay.beaver'
import random

def playRound():

    #This will print out the current phase.

    print("The come-out phase: ")
    print()

    #This will tell the user to hit enter to roll the dice.

    rollDice = raw_input("Hit ENTER to roll the dice...")

    #this will ensure that when a user hits enter, the program moves on.

    if rollDice == rollDice:

        #this will sum up two random integers to simulate two dice being thrown and record         the total.

        diceTotal = random.randint(1,6) + random.randint(1,6)

        #this will see if the numbers are 7 or 11, and if so, will let the user know they won.

        if diceTotal in (7,11):

            return "You rolled a", diceTotal
            return "You Win: Natural!"

        #this will see if numbers are 2, 3, or 12, and if so, will let user know they lost.

        if diceTotal in (2,3,12):

            return "You rolled a", diceTotal
            return "You Lose: Crap-Out!"

        #let user know what they rolled if conditions above are not met.

        return "You Rolled a", diceTotal

        #This will now start the point phase.

        print("The Point Phase:")
        print()

        #this will ask the user to hit enter to roll the dice.

        rollDice = raw_input("Hit ENTER to roll the dice...")

        #this will ensure that when the user hits enter, the dice will roll.

        if rollDice == rollDice:

            #this will add up the sum of two random numbers simulating dice and save to variable.

            diceTotalPoint = random.randint(1,6) + random.randint(1,6)

            #this will see if the roll is not 7 or the diceTotal from come-out phase.

            while diceTotalPoint not in (7, diceTotal):

                #This will continue to roll the dice, if 7 or the come-out phase number is not achieved.

                rollDice = raw_input("Hit ENTER to roll the dice...")

                if rollDice == rollDice:

                    diceTotalPoint = random.randint(1,6) + random.randint(1,6)

            #this will tell the user that if the dice roll is the same as the come-out phase,           it will be a hit and they win.

            if diceTotalPoint == diceTotal:

                return "You Rolled a", diceTotalPoint
                return "You Win: Hit!"

            #this will tell the user if they get a 7, and tell them they lose.

            if diceTotalPoint == 7:

                return "You Rolled a", diceTotalPoint
                return "You lose: Seven-Out!"