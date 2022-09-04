# cli-games/bnc.py

# Import the random method from the randint module
from random import randint

# Define roles
roles = ["Bear", "Ninja", "Cowboy"]

# Generate a random role using an array
computer = roles[randint(0,2)]

#STRETCH CHALLENGE - Break code into function ! 

#I created a function to increment the score by 1 in case of win OR reduce by 1 in
#case of player loss. Score cannot be negative.

score = 0 
current_score = 0

#Bool variables to track loss or win 
win = True     
lose = False

def keep_score (score, result):
    
    if result == False and score == 0: #if player lose but score is already at 0. To avoid score being negative 
        final_score = score 
    elif result == False and score > 0: 
        final_score = score - 1
    elif result == True:
        final_score = score + 1
    return final_score 



# Get player input

player = False

while player == False:

# get player input
    
    player = input("Bear, Ninja, or Cowboy? > ")
    
    # Compare computer and player role

    if computer == player:
         print("DRAW!")
    elif computer == "Cowboy":

          if player == "Bear":
            current_score = keep_score(score, lose)
            print("You lose!", player, "is shot by", computer, "score: ", current_score)
            
          else: # computer is cowboy, player is ninja
            current_score = keep_score(score, win)
            print("You win!", player, "defeats", computer, "score: ", current_score)

    elif computer =="Ninja":

          if player == "Bear":
            current_score = keep_score(score, win)
            print("You win!", player, "is eaten by", computer, "score: ", current_score)

          else: #computer is ninja and player is cowboy
            current_score = keep_score(score, lose)
            print("you lose!", player, "is defeated by", computer, "score: ", current_score)

    elif computer =="Bear":

          if player =="Cowboy":
            current_score = keep_score(score, win)
            print("you win!", player ,"shoots", computer, "score: ", current_score)

          else: #computer is bear and player is ninja
            current_score = keep_score(score, lose)
            print("You lose. . .", player, "is eaten by ", computer, "score: ", current_score)
    
    play_again = input("want to play again ? (yes/no))>")

    if play_again == "yes":
        player = False
        computer = roles[randint(0,2)]
    else:
        print(f"final score: {current_score}")
        break
