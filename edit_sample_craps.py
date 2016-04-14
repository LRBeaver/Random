__author__ = 'lyndsay.beaver'
import random

def playRound():
    print("The come-out phase: ")
    print()
    rollDice = input("Hit ENTER to roll the dice...")
    diceTotal = random.randint(1,6) + random.randint(1,6)

    if diceTotal in (7,11):
        print("You rolled a", diceTotal)
        print("You Win: Natural!")

    elif diceTotal in (2,3,12):
        print("You rolled a", diceTotal)
        print("You Lose: Crap-Out!")

    else:
        print("You rolled a", diceTotal)
        pointPhase(diceTotal)

def pointPhase(diceTotal):
    print("The Point Phase:")
    rollDice = input("Hit ENTER to roll the dice...")
    diceTotalPoint = random.randint(1,6) + random.randint(1,6)

    while diceTotalPoint not in (7, diceTotal):
        diceTotalPoint = random.randint(1,6) + random.randint(1,6)

        if diceTotalPoint == diceTotal:
            print("You Rolled a", diceTotalPoint)
            print("You Win: Hit!")
            break

        elif diceTotalPoint == 7:
            print("You Rolled a", diceTotalPoint)
            print("You lose: Seven-Out!")
        else:
            print("Keep Rolling")

def main():
    playRound()

main()