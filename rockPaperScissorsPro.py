# Monday fun - rockPaperScissorsPro

# Import libraries, modules
import random


def play():
    userInput = input("Press 'r' for rock, 'p' for paper and 's' for scissors!\n")
    computerChoice = random.choice(['r', 'p', 's'])

    print(f"Computer picked {computerChoice}.")

    if userInput == computerChoice: 
        return "Draw! Try again!"
    
    # Remember that rock > scissors, scissors > paper, paper > rock
    if findWinner(userInput, computerChoice):
        return "You're the winner! Congratulations!"
    
    return "Sorry, you lost!"

def findWinner(playerOne, playerTwo): 

    if (playerOne == 'r' and playerTwo == 's') or (playerOne == 's' and playerTwo == 'p') \
    or (playerOne == 'p' and playerTwo == 'r'):
        return True


print(play())


# Made with love.
# Check out Harry Mack on YouTube. 
# Have a great day.