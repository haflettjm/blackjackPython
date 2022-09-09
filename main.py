'''
    Small Python Project to create ASCII BlackJack game from scratch Idea inspired by big book of small python projects
    define scoring:
        Ace = 1 or 11
        Faces = 10
        Numbers = 1 - 10

    Try to get as close to 21 without going over.
                   Kings, Queens, and Jacks are worth 10 points.
                   Aces are worth 1 or 11 points.
                   Cards 2 through 10 are worth their face value.
                   (H)it to take another card.
                   (S)tand to stop taking cards.
                   On your first play, you can (D)ouble down to increase your bet
                   but must hit exactly one more time before standing.
                   In case of a tie, the bet is returned to the player.
                   The dealer stops hitting at 17.


'''

#Handles betting
def bet(money):
    amount = input(f'Please input how much you want to bet')

    if amount == 'QUIT':
        exit()
    elif type(amount) == 'int':
        if (amount <= money) and (amount > 0):
            return amount
        else:
            print(f'Invalid Bet amount Please input more then 0 or less then; {money}')
            bet(money)
    else:
        print('Invalid input please try again.')
        bet(money)


# Prints rules
def rules(money):
    print(f"""
        Try to get as close to 21 without going over.
                   Kings, Queens, and Jacks are worth 10 points.
                   Aces are worth 1 or 11 points.
                   Cards 2 through 10 are worth their face value.
                   (H)it to take another card.
                   (S)tand to stop taking cards.
                   On your first play, you can (D)ouble down to increase your bet
                   but must hit exactly one more time before standing.
                   In case of a tie, the bet is returned to the player.
                   The dealer stops hitting at 17.
                   You start with {money} total to bet with.
    """)

#game logic handler

def gameLoop(betAmnt, money):
    


#Handles repeated playing

def playAgain(gameState):

#Create Boilerplate for main function
def main():
    # Define current Money + Print Rules + Print Starting walllet size
    money = 5000
    rules(money)

    #initialize gameState
    gameState = 'go'

    while gameState != 'QUIT':
        #show current money
        print(f"Current Money: ", money)
        print("\n")

        #take bet
        betAmnt = bet(money)

        #run game logic
        gameLoop(betAmnt, money)

        playAgain(gameState)





if __name__ == '__main__':
    main()
