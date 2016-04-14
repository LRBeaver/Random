__author__ = 'lyndsay.beaver'
import random

def fillMarket():
    print("Creating the initial market ")
    print()
    newStocks = input("Hit ENTER to populate the market")
    startingStocks = {'ABC':10, 'XYZ': 15}
    showMarket(startingStocks)


def showMarket(startingStocks):
    print("Here is the starting market: ")
    print("There are " + str(len(startingStocks)) + " stocks in the market")
    print("ABC opens at: ", startingStocks['ABC'])
    print("XYZ opens at: ", startingStocks['XYZ'])
    print(' ')
    currentStocks=startingStocks
    newDay(currentStocks)

def newDay(currentStocks):
    print('New day starting.')
    print('Here is the market: ', currentStocks)
    currentStocks['ABC'] += 2
    print('Updated: ', currentStocks['ABC'])


def main():
    fillMarket()

main()