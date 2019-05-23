# -*- coding: utf-
import random
import sys
import re
global money
money = 500
#Defines the intro function
def intro():
    print("Hey there! Welcome to command-line Blackjack. This is a very basic",
          "form of the popular card-game Blackjack. The purpose is to get as",
          "close to 21 'points' as possible without going over (busting). If the",
          "dealer busts, you win right away. Splitting isn't an option, and neither",
          "is insurance. Sorry about that. Good luck!")

#This is a function that picks the cards of the player
def cardDrawer(deck):
    a = random.randint(0,51)
    value = deck.pop(a)
    b = random.randint(0,50)
    valueTwo = deck.pop(b)
    hand = [value, valueTwo]
    print("Here's your hand!")
    print(hand)
    return hand

#Function that picks cards of the dealer
def dealerDrawer(deck):
    #remove the player's hand values from the Deck
    a = random.randint(0,49)
    value1 = deck.pop(a)
    b = random.randint(0,48)
    value2 = deck.pop(b)
    dealerHand = [value1, value2]
    return dealerHand

#Shows the first card in the dealer's hand
def dealerHandShower(hand):
    print("Here's the top card on the dealer's hand")
    print(hand[0])

#Calculates the value of a given hand
def valueCalculator(hand):
    value = 0
    valueList = []
    if hand != True:
        for i in range(0,len(hand)):
            numericValue = (hand[i].split()[0])
            valueList.append(numericValue)
            for i in range(0,len(valueList)):
                if valueList[i] == "Jack" or valueList[i] == "Queen" or valueList[i] == "King":
                    valueList[i] = "10"
                if valueList[i] == "Ace":
                    valueList[i] = "11"
      
        for i in valueList:
            value += int(i)
    
    if value > 21:
        for i in range (0, len(valueList)):
            if valueList[i] == "11":
                valueList[i] = "1"
                break
    if hand != True:
        return value
    else: 
        return 21

#checks to see if the player/dealer has won after the initial deal
def victoryCheck(value):
    if value == 21:
        return True
    else:
        return False

#Gives the player the decision to hit or stand
def decisionMaker(deck, hand):
    flag = False
    while flag == False:
        decision = input("Type 'hit' to get another card or 'stand' to stand!")
        if decision == "hit":
            a = random.randint(0,len(deck)-1)
            card = deck.pop(a)
            hand.append(card)
            print("Here's your new hand")
            print(hand)
            print("The value of your hand is", valueCalculator(hand))
            if valueCalculator(hand) == 21:
                return True
            if valueCalculator(hand) > 21:
                print("Ooh sorry... looks like you busted")
                return False
        elif decision == "stand":
            flag = True
            return hand
        
    
            
#checks to see if the bet is valid
def betChecker(currentBet):
    flag = False
    while flag == False:
        try:
            int(currentBet)
            if currentBet > money or currentBet <= 0:
                raise Exception
            return currentBet
        except:
            currentBet = input("Type 'stop' if you're sure you want to quit, or put a whole number, positive, bet to keep playing")
            if currentBet == "stop":
                return False
            
    
def finalDisplay(hand, dealerHand):
    print("Here's your new hand (if you hit)")
    print(hand)
    print("The value of your hand is", valueCalculator(hand))
    print("")
    print("Here's the Dealer's hand")
    print(dealerHand)
    print("The value of the dealer's hand is", valueCalculator(dealerHand))

def winCondition(playerValue, dealerValue):
    if playerValue == dealerValue:
        return "Tie"
    elif playerValue > dealerValue:
        return "Win"
    else:
        return "Lose"

def playerChecker(playerName):
    flag = False
    readFile = open("scoreboard.txt")
    for line in readFile:
        if playerName in line:
            flag = True
            lineInfo = line.split()
            currentVal = int(lineInfo[1])
    readFile.close()
    if flag == False:
        return 500
    else:
        return currentVal

                    
    



intro()
playerName = input("Why don't you start by telling me your name?")
money = playerChecker(playerName)

flag = False
while flag == False:
    print("")
    print("You currently have", money, "dollars")
    deck = [
         "2 of Spades", "2 of Clubs", "2 of Diamonds", "2 of Hearts",
         "3 of Spades", "3 of Clubs", "3 of Diamonds", "3 of Hearts",
         "4 of Spades", "4 of Clubs", "4 of Diamonds", "4 of Hearts",
         "5 of Spades", "5 of Clubs", "5 of Diamonds", "5 of Hearts",
         "6 of Spades", "6 of Clubs", "6 of Diamonds", "6 of Hearts",
         "7 of Spades", "7 of Clubs", "7 of Diamonds", "7 of Hearts",
         "8 of Spades", "8 of Clubs", "8 of Diamonds", "8 of Hearts",
         "9 of Spades", "9 of Clubs", "9 of Diamonds", "9 of Hearts",
         "10 of Spades", "10 of Clubs", "10 of Diamonds", "10 of Hearts",
         "Jack of Spades", "Jack of Clubs", "Jack of Diamonds", "Jack of Hearts",
         "Queen of Spades", "Queen of Clubs", "Queen of Diamonds", "Queen of Hearts",
         "King of Spades", "King of Clubs", "King of Diamonds", "King of Hearts",
         "Ace of Spades", "Ace of Clubs", "Ace of Diamonds", "Ace of Hearts"
         
    ]
    print("")
    currentBet = input("Type how much you want to bet (whole number, less than your money), or type 'stop' to quit playing!")
    a = betChecker(currentBet)
    if a == False:
        fileWriter = open("scoreboard.txt","a")
        fileWriter.write(playerName + " " + str(money) + "\n")
        fileWriter.close()
        sys.exit("Thanks for playing!")
    else:
        currentBet = a
    playerHand = cardDrawer(deck)
    dealerHand = dealerDrawer(deck)
    value = valueCalculator(playerHand)
    print("The value of your hand is", value)
    print("")
    
    dealerHandShower(dealerHand)
    dealerValue = valueCalculator(dealerHand)
    playerWin = victoryCheck(value)
    dealerWin = victoryCheck(dealerValue)
    
    if playerWin and dealerWin:
        print("Oh. Looks like it's a tie.")
    elif playerWin:
        print("Nice, you got blackjack!")
        money += 1.5 * int(currentBet)
    elif dealerWin:
        print(dealerHand)
        print("Yikes, looks like the dealer has Blackjack...sorry")
        money -= int(currentBet)
    else:
        playerHand = decisionMaker(deck, playerHand)
        if isinstance(playerHand, list):
            finalDisplay(playerHand, dealerHand)
            playerValue = valueCalculator(playerHand)
            dealerValue = valueCalculator(dealerHand)
            winData = winCondition(playerValue, dealerValue)
            if playerValue > dealerValue:
                print("")
                print("Congratulations, you won", int(currentBet) * 2, "dollars")
                money += int(currentBet)
            elif dealerValue > playerValue:
                print("Sorry, looks like you lost that one.")
                money -= int(currentBet)
            else:
                print("Well, looks like that one was a tie")
        elif playerHand == True:
            print("Looks like you have 21 points... you should probably stop hitting now")
            finalDisplay(playerHand, dealerHand)
            playerValue = valueCalculator(playerHand)
            dealerValue = valueCalculator(dealerHand)
            winData = winCondition(playerValue, dealerValue)
            if playerValue > dealerValue:
                print("")
                print("Congratulations, you won", int(currentBet) * 2, "dollars")
                money += int(currentBet)
            else:
                print("Ooh sorry... looks like a tie")
        else:
            money -= int(currentBet)
    
    if money == 0:
        print("Wow... you're bad at this...here's a pick me-up")
        money = 100
        

   


    
    
    
    
    
    
    
    
    
    
    
    
    
